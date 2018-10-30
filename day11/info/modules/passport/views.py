# 导入flask内置的对象
from flask import request, jsonify, current_app, make_response, session
from . import passport_blue
# 导入captcha扩展，生成图片验证码
from info.utils.captcha.captcha import captcha
# 导入自定义的状态码
from info.utils.response_code import RET
# 导入redis实例
from info import redis_store, constants
# 导入正则
import re, random
# 导入云通讯扩展
from info.libs.yuntongxun import sms
from info.models import User, db
from datetime import datetime


@passport_blue.route("/image_code")
def generate_image_code():
    """
    生成图片验证码
    1、获取参数，uuid，使用request.args查询字符串参数
    2、判断参数是否存在，如果不存在，直接return
    3、调用captcha工具，生成图片验证码
    name,text,image
    4、在redis数据库中存储图片验证码的text内容
    5、返回图片给前端

    :return:
    """
    # 获取查询字符串形式的参数
    image_code_id = request.args.get("image_code_id")
    # 如果参数不存在，直接return
    if not image_code_id:
        return jsonify(errno=RET.PARAMERR, errmsg='参数缺失')
    # 调用captcha生成图片验证码
    name, text, image = captcha.generate_captcha()
    # 存储图片验证码的text到redis数据库中
    try:
        # redis_store.setex('ImageCode_' + image_code_id,300,text)
        redis_store.setex('ImageCode_' + image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存数据失败')
    else:
        # 返回图片
        response = make_response(image)
        # 设置响应的类型为image/jpg
        response.headers['Content-Type'] = 'image/jpg'
        return response


@passport_blue.route('/sms_code', methods=['POST'])
def send_sms_code():
    """
    发送短信
    获取参数---检查参数---业务处理---返回结果
    1、获取参数，mobile(用户的手机号)，image_code(用户输入的图片验证码),image_code_id(UUID)
    2、检查参数的完整性
    3、检查手机号格式，正则
    4、尝试从redis中获取真实的图片验证码
    5、判断获取结果，如果不存在图片验证码已经过期
    6、需要删除redis中存储的图片验证码,图片验证码只能比较一次，本质是只能对redis数据库get一次。
    7、比较图片验证码是否正确
    8、生成短信验证码，六位数
    9、存储在redis数据库中
    10、调用云通讯，发送短信
    11、保存发送结果，判断发送是否成功
    12、返回结果

    :return:
    """
    # 获取前端传入的参数
    mobile = request.json.get('mobile')
    image_code = request.json.get('image_code')
    image_code_id = request.json.get('image_code_id')
    # 检查参数的完整性
    # if not mobile and image_code and image_code_id:
    if not all([mobile, image_code, image_code_id]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数不完整')
    # 校验手机号131123456789
    if not re.match(r'1[3456789]\d{9}$', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号格式错误')
    # 尝试从redis中获取真实的图片验证码
    try:
        real_image_code = redis_store.get('ImageCode_' + image_code_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='获取数据失败')
    # 判断获取结果是否存在
    if not real_image_code:
        return jsonify(errno=RET.NODATA, errmsg='图片验证码已过期')
    # 删除redis中存储的图片验证码，因为图片验证码只能get一次，只能比较一次
    try:
        redis_store.delete('ImageCode_' + image_code_id)
    except Exception as e:
        current_app.logger.error(e)
    # 比较图片验证码是否正确
    if real_image_code.lower() != image_code.lower():
        return jsonify(errno=RET.DATAERR, errmsg='图片验证码不一致')
    # 生成短信验证码
    sms_code = '%06d' % random.randint(0, 999999)
    print(sms_code)
    # 存储在redis中，key可以拼接手机号
    try:
        redis_store.setex('SMSCode_' + mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存数据失败')

    # 调用云通讯发送短信
    try:
        ccp = sms.CCP()
        # result = ccp.send_template_sms(mobile, [sms_code, constants.SMS_CODE_REDIS_EXPIRES / 60], 1)
        result = ccp.send_template_sms(mobile, [sms_code, constants.SMS_CODE_REDIS_EXPIRES], 1)
        # result = ccp.send_template_sms('18342910537', ['1234', 5], 1)

    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg='发送短信异常')

    # 判断result是否成功
    if result == 0:
        return jsonify(errno=RET.OK, errmsg='发送成功')
    else:
        return jsonify(errno=RET.THIRDERR, errmsg='发送失败')


@passport_blue.route('/register', methods=['POST'])
def register():
    """
    用户注册
    获取参数---检查参数---业务处理---返回结果
    1、获取前端ajax发送的post请求的三个参数，mobile，sms_code,password
    2、检查参数的完整性
    3、检查手机号的格式
    用户是否注册？
    4、尝试从redis数据库中获取真实的短信验证码
    5、判断获取结果是否过期
    6、比较短信验证码是否正确，因为短信验证码可以比较多次，图片验证码只能比较一次
    7、删除redis数据库中存储的短信验证码
    用户是否注册？
    8、构造模型类对象,准备保存用户信息
    user = User()
    user.password = password
    9、提交数据到mysql数据库中，如果发生异常，需要进行回滚
    10、缓存用户信息，使用session对象到redis数据库中；
    11、返回结果
    """
    print('123456')
    mobile = request.json.get('mobile')
    sms_code = request.json.get('sms_code')
    password = request.json.get('password')
    if not all([mobile, sms_code, password]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")
    if not re.match(r'^1[3456789]\d{9}$', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg="手机格式错误")
    try:
        real_sms_code = redis_store.get("SMSCode_" + mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="获取数据失败")
    if not real_sms_code:
        return jsonify(errno=RET.NODATA, errmsg="短信验证码已过期")
    try:
        redis_store.delete('SMSCode_' + mobile)
    except Exception as e:
        current_app.logger.error(e)
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="查询数据失败")
    else:
        if user is not None:
            return jsonify(errno=RET.DATAEXIST, errmsg="手机号已注册")
    # if mobile not register , structure model object
    user = User()
    user.nick_name = mobile
    # used models's generate_password_hash, realize password encryption
    user.password = password
    user.mobile = mobile
    try:
        db.session.add(user)
        db.session.commit()
        print('add db successful')
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(error=RET.DBERR, errmsg="保存用户信息失败")
    session['user_id'] = user.id
    session['nick_name'] = mobile
    session['mobile'] = mobile
    return jsonify(errno=RET.OK, errmsg='OK')


@passport_blue.route('/login', methods=['POST'])
def login():
    mobile = request.json.get('mobile')
    password = request.json.get('password')
    if not all([mobile, password]):
        return jsonify(errno=RET.DATAERR, errmsg="参数不完整")
    if not re.match(r'^1[23456789]\d{9}$', mobile):
        return jsonify(errno=RET.DATAERR, errmsg="手机号格式不正确")
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="查询用户数据失败")
    if user is None or not user.check_password(password):
        return jsonify(errno=RET.DATAERR, errmsg="用户名或密码错误")
    user.last_login = datetime.now()
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg="保存数据失败")
    session['user_id'] = user.id
    session['nick_name'] = user.nick_name
    session['mobile'] = user.mobile
    return jsonify(errno=RET.OK, errmsg='OK')


@passport_blue.route('/logout', methods=["POST"])
def logout():
    """
    clear session's information
    :return:
    """
    session.pop('user_id', None)
    session.pop('nick_name', None)
    session.pop('mobile', None)

    return jsonify(errno=RET.OK, errmsg="OK")

    pass

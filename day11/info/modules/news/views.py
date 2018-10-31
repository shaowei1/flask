# 导入flask内置的对象
from flask import session, render_template, current_app, jsonify, request, g
# 导入蓝图对象
from . import news_blue

from info import constants
from info.utils.response_code import RET
from info.utils.common import login_required

from info.models import User, Category, News, db


@news_blue.route("/")
@login_required
def index():
    # session['baidu'] = 2018

    user = g.user
    try:
        categories = Category.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询新闻分类数据失败')

    if not categories:
        return jsonify(errno=RET.NODATA, errmsg="无新闻分类数据")

    category_list = []
    for category in categories:
        category_list.append(category.to_dict())

    # new click ranking
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询新闻点击排行数据失败')

    if not news_list:
        return jsonify(errno=RET.NODATA, errmsg='无新闻点击排行数据')

    news_click_list = []
    for news in news_list:
        news_click_list.append(news.to_dict())

    data = {
        'user_info': user.to_dict() if user else None,
        'category_list': category_list,
        'news_click_list': news_click_list,
    }

    return render_template('news/index.html', data=data)


@news_blue.route('/news_list')
def get_news_list():
    """
    新闻列表数据
    1、获取参数，cid('1')/page('1')/per_page('10')
    request.args.get()
    2、检查参数，转换数据类型
    3、根据分类id查询新闻列表,按照新闻发布时间排序，分页
    4、如果新闻有分类，根据分类查询
    if cid > 1:
        paginate = News.query.filter(News.category_id==cid).order_by(News.create_time.desc()).paginate(page,per_page,False)
    else:
        paginate = News.query.filter().order_by(News.create_time.desc()).paginate(page,per_page,False)
    5、如果新闻是最新，默认查询所有
    paginate = News.query.filter().order_by(News.create_time.desc()).paginate(page,per_page,False)
    6、获取分页后的新闻列表、总页数、当前页数
    7、定义容器，遍历查询结果
    8、返回数据
    :return:
    """
    cid = request.args.get("cid", '1')
    page = request.args.get('page', '1')
    per_page = request.args.get('per_page', '10')

    try:
        cid, page, per_page = int(cid), int(page), int(per_page)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='参数类型错误')

    filters = []

    if cid > 1:
        filters.append(News.category_id == cid)
    try:
        paginate = News.query.filter(*filters).order_by(News.create_time.desc()).paginate(page, per_page, False)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询新闻列表数据失败')

    news_list = paginate.items
    current_page = paginate.page
    total_page = paginate.pages

    news_dict_list = []

    for news in news_list:
        news_dict_list.append(news.to_dict())

    data = {
        'news_dict_list': news_dict_list,
        'total_page': total_page,
        'current_page': current_page,
    }
    # print(data)
    return jsonify(errno=RET.OK, errmsg='OK', data=data)


@news_blue.route('/<int:news_id>')
@login_required
def news_detail(news_id):
    """
    news_detail data display
    :param news_id:
    :return:
    """
    user = g.user

    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询新闻点击排行数据失败')

    if not news_list:
        return jsonify(errno=RET.NODATA, errmsg='无新闻点击排行数据')

    news_click_list = []

    for news in news_list:
        news_click_list.append(news)

    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询新闻详情数据失败')

    if not news:
        return jsonify(errno=RET.NODATA, errmsg='无新闻详情数据')
    news.clicks += 1

    try:
        db.session.add(news)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='保存数据失败')

    is_collected = False
    if user and news in user.collection_news:
        is_collected = True

    data = {
        'user_info': user.to_dict() if user else News,
        'news_click_list': news_click_list,
        'news_detail': news.to_dict(),
        'is_collection': is_collected,
    }

    return render_template('news/detail.html', data=data)
    pass


# 项目logo图标加载，浏览器会默认请求。
# 如果图标加载不出来？？
# 1、清除浏览器缓存
# 2、浏览器彻底退出重启
# http://127.0.0.1:5000/favicon.ico
@news_blue.route('/favicon.ico')
def favicon():
    # 通过应用上下文对象，调用发送静态文件给浏览器
    return current_app.send_static_file('news/favicon.ico')

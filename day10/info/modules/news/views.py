# 导入flask内置的对象
from flask import session, render_template, current_app
# 导入蓝图对象
from . import news_blue

from info.models import User


@news_blue.route("/")
def index():
    # session['baidu'] = 2018
    user_id = session.get('user_id')
    user = None
    try:
        user = User.query.filter_by(id=user_id).first()
    except Exception as e:
        current_app.logger.error(e)

    data = {
        'user_info': user.to_dict() if user else None
    }

    return render_template('news/index.html', data=data)


# 项目logo图标加载，浏览器会默认请求。
# 如果图标加载不出来？？
# 1、清除浏览器缓存
# 2、浏览器彻底退出重启
# http://127.0.0.1:5000/favicon.ico
@news_blue.route('/favicon.ico')
def favicon():
    # 通过应用上下文对象，调用发送静态文件给浏览器
    return current_app.send_static_file('news/favicon.ico')

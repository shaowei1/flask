# 源程序app.py文件:
# 我们有一个博客程序,前台界面需要的路由为:首页,列表,详情等页面
# 如果博主需要编辑博客,要进入后台进行处理:后台主页,编辑,创建,发布博客

from flask import Flask, Blueprint

app = Flask(__name__)

# import blueprint object
from demo2_private import private
from demo2_admin import admin

# from demo2_admin import admin_home, edit, publish, new
# from modules import * 容易导错(一个函数在多个文件中重名)
# from demo2_admin import *  # 一个一个导入，不可以，可能是由于优先级问题

# register blueprint object
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(private, url_prefix='/private')


@app.route('/')
def index():
    """首页"""
    return 'index'


@app.route('/list')
def list():
    """列表页面"""
    return 'list'


@app.route('/detail')
def detail():
    """详情页面"""
    return 'detail'


if __name__ == '__main__':
    print(app.url_map)
    app.run()

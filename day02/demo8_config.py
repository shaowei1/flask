from flask import Flask, make_response, request, session
# Flask class
# session object
from config import Config, config_dict

app = Flask(__name__)
# config是flask内置的配置对象
# 实现形式三种：
# 1、加载配置对象,
# app.config.from_object(Config)
app.config.from_object(config_dict['production'])  # 扩展性更强, 可以选production or development


# 2、加载配置文件
# app.config.from_pyfile('config.ini')

# 3、加载环境变量
# SETTINGS|path of config.ini --> edit configuration -> environment variable
# app.config.from_envvar('SETTINGS')


# 设置cookie
@app.route('/')
def index():
    # 使用flask内置的响应对象来设置cookie
    response = make_response('set cookie')
    response.set_cookie('itcast', 'python33', max_age=3600)  # 设置cookie,max_age表示有效期，单位秒, 3600 one hour, 86400 one day
    return response  # 返回响应


# 获取cookie
@app.route('/get')
def get_cookie():
    # request是flask内置的对象，用来获取客户端的请求信息
    # cookies是对象的属性
    itcast = request.cookies.get('itcast')
    return itcast


# session的设置
@app.route('/session')
def set_session():
    # session是flask内置的上下文对象，用来实现状态保持中的session
    session['itcast'] = 'python33'
    return 'set session success'


# session的获取
@app.route('/getss')
def get_session():
    itcast = session.get('itcast')
    return itcast


if __name__ == '__main__':
    # 读取配置
    # cof = app.config.get(app.debug)
    # print(cof)
    # 在视图函数中使用current_app.config.get()
    # Flask 应用程序将一些常用的配置设置成了应用程序对象的属性，也可以通过属性直接设置 / 获取某些配置：app.debug = True
    # app.run(host="0.0.0.0", port=5000, debug=True)
    app.run()

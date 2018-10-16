from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def index():
    # abort(500)
    return []


# 请求钩子：相当于python中的初始化函数__init__和析构函数__del__
# 在请求前执行，两个
@app.before_first_request
def before_first_request():
    print('before first request run----')  # 在第一次请求前执行


@app.before_request
def before_first_request():
    print('before request run----')  # 在每次请求执行


# 相当于django and spider 中的中间件
# 在请求后执行，两个
# @app.after_request
# def after_request(response):
#     print('after request run---') # 没有异常(web服务器内部错误)的情况下，会执行
#     return response
# @app.teardown_request
# def teardown_request(e):
#     print('teardown request run---') # 即使有异常，也执行


if __name__ == '__main__':
    app.run(debug=True)

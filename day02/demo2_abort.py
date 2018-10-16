from flask import Flask, abort

app = Flask(__name__)


# normal use
# try:
#     print('a')
# except Exception as e:
#     abort(404)

# abort函数：本质是异常处理，功能类似于python中的raise语句，用来抛出异常信息，会终止程序的运行。

# 结论：abort函数只能抛出符合http协议的异常状态码（4开头或5开头）
# 作用：用来进行异常信息的处理，比如自定义错误信息。
@app.route('/')
def index():
    # abort函数参数表示状态码
    abort(404)
    # HTTP/1.0 200 OK
    # after will not be execute
    return 'hello world', 666


# 自定义错误信息
# 用来接收abort抛出的异常信息，用来错误处理
@app.errorhandler(404)
def err_handler(e):
    return '<h2>页面不存在，请访问***页面！！！</h2>%s' % e


if __name__ == '__main__':
    app.run(debug=True)

'''
除0错误
'''
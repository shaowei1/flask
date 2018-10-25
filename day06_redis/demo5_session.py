from flask import Flask, session
# 使用扩展包flask_session
from flask_session import Session
from redis import StrictRedis

app = Flask(__name__)
# 密钥
app.config['SECRET_KEY'] = 'ASDFASDF/ASDFA1234SDMF234;ASDFQWERWRWETRERTFHFGJ234123412'
# 扩展包提供配置，指定session信息存储的位置
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = StrictRedis()
app.config['SESSION_USE_SIGNER'] = True
# Flask内置的指定session信息存储的有效期
app.config['PERMANENT_SESSION_LIFETIME'] = 3600

# 实例化Session对象
Session(app)


@app.route('/')
def index():
    session['baidu'] = '2018'
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)

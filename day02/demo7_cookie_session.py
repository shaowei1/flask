from flask import Flask, make_response, request, session

app = Flask(__name__)

# config是flask内置的配置对象，
# 设置SECRET_KEY配置项，设置session信息时需要使用此配置项
app.config['SECRET_KEY'] = '2018'
# 根据密钥来生成session编码信息，加密后的字符串。
# session=eyJpdGNhc3QiOiJweXRob24zMyJ9.DqXvnw.Dvb9iFcQYUAho6cBGvjgThZilxc;
'''
SECRET_KEY 配置变量是通用密钥, 可在 Flask 和多个第三方扩展中使用. 如其名所示, 加密的强度取决于变量值的机密度. 不同的程序要使用不同的密钥, 而且要保证其他人不知道你所用的字符串.

SECRET_KEY 的作用主要是提供一个值做各种 HASH, 我没有实际研究过源码, 不同框架和第三方库的功能也不尽相同, 我不能给出准确的答案, 但是主要的作用应该是在其加密过程中作为算法的一个参数(salt 或其他). 所以这个值的复杂度也就影响到了数据传输和存储时的复杂度.

另外, 考虑到安全性, 这个密钥是不建议存储在你的程序中的. 最好的方法是存储在你的系统环境变量中, 通过 os.getenv(key, default=None) 获得.
'''

# 状态保持：服务器需要记录用户登录信息。
"""
概念：cookie和session：都是基于键值对的字符串，用来记录用户信息；
区别：
cookie: key/value键值都存储在浏览器中，不安全；

session: key基于cookie实现，键存储在浏览器中，value值存储在服务器；

"""
'''
Cookie:
Cookie是由服务器端生成，发送给客户端浏览器，浏览器会将Cookie的key/value保存，下次请求同一网站时就发送该Cookie给服务器（前提是浏览器设置为启用cookie）。
Cookie的key/value可以由服务器端自己定义。
Cookie基于域名安全，不同域名的Cookie是不能互相访问的
当浏览器请求某网站时，会将本网站下所有Cookie信息提交给服务器，所以在request中可以读取Cookie信息

Session:
对于敏感、重要的信息，建议要存储在服务器端，不能存储在浏览器中，如用户名、余额、等级、验证码等信息
在服务器端进行状态保持的方案就是Session
Session依赖于Cookie

'''


# 设置cookie
@app.route('/')
def index():
    # 使用flask内置的响应对象来设置cookie
    # 通过make_response创建响应对象，
    response = make_response('set cookie')
    # 调用响应对象的set_cookie方法设置cookie信息
    response.set_cookie('baidu', 'python', max_age=3600)  # 设置cookie,max_age表示有效期，单位秒
    response.set_cookie('taobao', 'ruby', max_age=3600)
    '''Cookies
    Name    baidu
    Content python
    Domain  127.0.0.1.
    Path    /
    Send for And kind of connection
    Created Tuesday, October 16, 2018 at 9:02:02 PM
    Expires Tuesday, October 16, 2018 at 10:02:02 PM
    '''
    return response  # 返回响应


# 获取cookie
@app.route('/get')
def get_cookie():
    # request是flask内置的对象，用来获取客户端的请求信息
    # cookies是对象的属性
    # 通过request对象的cookies属性获取客户端发送的cookie数据
    baidu = request.cookies.get('baidu')
    taobao = request.cookies.get('taobao')
    return 'baidu: %s, taobao: %s' % (baidu, taobao)


# session的设置
# 验证session 使用postman + postman Interceptor
@app.route('/session')
def set_session():
    # session是flask内置的上下文对象，用来实现状态保持中的session
    session['baidu'] = 'python'
    session['taobao'] = 'ruby'
    return 'set session success'


# session的获取
@app.route('/getsession', methods=['POST', 'GET'])
def get_session():
    baidu = session.get('baidu')
    taobao = session.get('taobao')
    return 'baidu: %s, taobao: %s' % (baidu, taobao)


if __name__ == '__main__':
    app.run(debug=True)

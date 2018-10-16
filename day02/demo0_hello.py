from flask import Flask

app = Flask(__name__)

'''
1. who am I?
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36
用户代理: 浏览器名 系统名 64 kernel version number browser
2. where do I come from?
Referer: https://www.baidu.com/
3. where are I going to go?
Request
'''


@app.route('/')
def index():
    # int a = 1
    # a = 1
    # print('hello world')
    # return [] # 'list' object is not callable
    # return {} # 'dict' object is not callable
    # return 1 # 'int' object is not callable
    return 'hello world'  # 可以
    # return ('1',) # 可以


if __name__ == '__main__':
    app.run(debug=True)

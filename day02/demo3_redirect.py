from flask import Flask, redirect, url_for
# 首字母大写是类，小写函数
app = Flask(__name__)


# 重定向：重新发起网络请求。
# 作用：当网站文件或目录发生变化的时候，可以使用重定向。
@app.route('/')
def index():
    url = 'http://www.11.cn'
    # 接收的参数location表示具体的url地址。
    # return redirect(url)
    return redirect('http://www.baidu.com')


# url_for:反向解析
@app.route('/abc')
def demo_url_for():
    # url_for接收的参数表示端点，即视图函数名的字符串形式
    # url_for 反向解析，从'index'--see> '/'
    return redirect(url_for('index'))


if __name__ == '__main__':
    print(app.url_map)
    '''
    Map([<Rule '/abc' (HEAD, GET, OPTIONS) -> demo_url_for>,
 <Rule '/' (HEAD, GET, OPTIONS) -> index>,
 <Rule '/static/<filename>' (HEAD, GET, OPTIONS) -> static>])
     
    '''
    app.run(debug=True)

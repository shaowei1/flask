from flask import Flask, request
from werkzeug.routing import BaseConverter, Rule, Map, MapAdapter

app = Flask(__name__)


# request常用的属性：args/form/files/method/url/cookies/headers
@app.route('/', methods=['GET', 'POST'])
def index():
    # 输出请求方法、请求url、请求头
    print(request.method)
    print(request.url)
    print(request.headers)

    # # 获取文件对象
    image = request.files.get('image')
    # 保存文件
    image.save('./beautiful.jpg')
    # 返回结果
    return 'save image success'

    # 如果是get请求：
    # if request.method == 'GET':
    #     # 获取浏览器传入的查询字符串参数
    #     # http://127.0.0.1:5000/?name=python33&age=20
    #     name = request.args.get('name')
    #     age = request.args.get('age')
    #     print(name, age)
    #     return 'GET response'
    # # 如果是post请求：
    # else:
    #     # form 在请求体里
    #     baidu = request.form.get('baidu')
    #     age = request.form.get('age')
    #     print(baidu, age)
    #     return 'POST response'


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)

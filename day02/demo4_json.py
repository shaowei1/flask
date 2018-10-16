from flask import Flask, jsonify
import json

app = Flask(__name__)

# json:轻量级的数据交互格式，不是数据类型。
# 概念：本质是字符串，基于键值对形式的字符串。
# 作用：用来实现跨平台跨语言的数据交互，传输数据。
"""


python:
数值、字符串、列表、字典、集合、元组。

python中对json数据的处理：
json.dumps() 把字典转成json字符串，操作的是变量，存储在计算机内存中，f = '123'
json.loads() 把json字符串转成字典,

json.dump() 把字典转成json字符串,操作的是文件对象(具有read和write方法的对象)，f=open('a.txt'.'r') f是文件对象
json.load() 把json字符串转成字典,操作的是文件对象，计算机硬盘。

javascript：
数组、字符串、数值、对象、undefined、None、NUll

JSON.stringify(params) 把前端对象转成json字符串
JSON.parse(resp) 把json字符串转成对象


微信：使用的xml格式的数据传输。
xmltodict模块pip install xmltodict
unparse / parse

'{"name":"python33","age":18}'

<xml>
    <name>python33</name>
    <age>18</age>
    <gender>MAN</gender>
</xml>

"""


@app.route('/')
def index():
    # 定义字典
    data = {
        'name': 'python33',
        'age': 18
    }
    # return data # 不能返回字典
    # jsonify把字典转成json字符串
    return jsonify(data)  # Content-Type: application/json
    # return json.dumps(data) # Content-Type: text/html;


if __name__ == '__main__':
    app.run(debug=True)

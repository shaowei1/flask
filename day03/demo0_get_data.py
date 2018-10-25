'''
    2. 使用Flask实现web程序，定义视图实现以下功能：
    • 1）从url地址中提取字符串
2）从url地址中提取int参数
3）获取客户端传递的查询字符串参数
4）获取客户端传递的表单数据
5）获取客户端传递的json数据
6）响应时进行页面的重定向
7）响应时返回json数据

    • 涉及知识点:
    • 1）使用路由转换器从url中提取参数(字符串和int)
2）request对象的属性:
	args: 保存客户端传递的查询字符串数据;
	form: 保存客户端传递的表单类型数据;
	body: 保存客户端传递的请求体数据;
3）视图的响应:
	使用redirect进行页面重定向;
	使用jsonify返回json数据;
'''

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/orders/<order_id>')
def demo0(order_id):
    """从url地址中提取字符串参数"""
    return 'order_id: %s' % order_id


@app.route('/orders/<int:user_id>')
def demo1(user_id):
    """从url地址中提取int参数"""
    return 'user_id: %s' % user_id


# /get_args?a=<参数a>&b=<参数b>
@app.route('/get_query_data')
def demo2():
    """获取客户端传递的字符串参数"""
    a = request.args.get('a')
    b = request.args.get('b')
    return 'a: %s, b: %s' % (a, b)


# /get_form_data
# form数据如下:
# {
#    "username": "<用户名>",
#    "password": "<密码>"
# }
@app.route('/get_form_data', methods=["GET", "POST"])
def demo3():
    """获取客户端传递的表单数据"""
    username = request.form.get('username')
    password = request.form.get('password')
    return 'username: %s, password: %s' % (username, password)


# /get_json_data
# json数据如下:
# {
#    "username": "<用户名>",
#    "password": "<密码>"
# }
@app.route('/get_json_data', methods=["GET", "POST"])
def demo4():
    """获取客户端传递的json数据"""
    req_data = request.data  # bytes

    # convert bytes to string
    req_data = req_data.decode()

    # convert json_string to dict
    import json
    req_dict = json.loads(req_data)

    # get params
    username = req_dict.get('username')
    password = req_dict.get('password')
    return 'username: %s, password: %s' % (username, password)


# /redirect
from flask import redirect, url_for


@app.route('/redirect')
def demo5():
    """页面重定向"""
    # 重定向到同一域名底下
    return redirect('/orders/1')


# /json
from flask import jsonify


@app.route('/json')
def demo6():
    """返回json数据"""
    resp = {
        'id': 1,
        'name': 'yangixnyue',
        'age': 21
    }
    return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True)

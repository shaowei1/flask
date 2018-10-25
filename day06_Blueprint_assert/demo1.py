from flask import Flask
# 导入蓝图对象
from demo1_temp_file import api

app = Flask(__name__)
# 3　注册蓝图对象
app.register_blueprint(api)

"""
项目按功能可以划分模块：
订单、商品、用户模块等等
orders:http://127.0.0.1:5000/orders/
goods:http://127.0.0.1:5000/goods/
api:http://127.0.0.1:5000/api/

"""


# add_url_rule('/', 'index', index')
@app.route('/')
def index():
    return index


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)

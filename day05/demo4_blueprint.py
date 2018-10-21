from flask import Flask
from temp_detail import api

app = Flask(__name__)

# 3、注册蓝图对象给程序实例app
app.register_blueprint(api)


@app.route('/')
def index():
    return 'index'


@app.route('/list')
def list():
    return 'list'


if __name__ == '__main__':
    # 导包不能解决路由映射的问题
    from temp_detail import detail

    print(app.url_map)
    app.run(debug=True)

# 导入render_template
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # 给模板传入数据
    data = 'baidu'
    # 传入字典
    dict_data = {'name': 'python', 'age': 18}
    # 传入列表
    list_data = [6, 3, 7, 13, 21, 18]
    # 调用Jinja2模板引擎
    # Mark directory as -> Template folder --> jinja2
    # setting -> template language
    return render_template('demo3_template.html', data=data, dict_data=dict_data, list_data=list_data)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('demo5_filter.html')


# 自定义过滤器
# 需求：实现列表反转
# def list_reverse(ls):
#     temp_list = list(ls)
#     temp_list.reverse()
#     return temp_list

# 添加自定义过滤器给模板
# 结论：自定义过滤器和内置过滤器重名，会覆盖内置过滤器。
# app.add_template_filter(list_reverse,'list_reverse')


# 通过装饰器形式实现自定义过滤器
@app.template_filter('list_reverse2')
def list_reverse(ls):
    temp_list = list(ls)
    temp_list.reverse()
    return temp_list


if __name__ == '__main__':
    app.run(debug=True)

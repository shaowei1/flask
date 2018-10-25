'''
    • 功能要求：
    • 在模板文件中使用my_list列表数据，内容如下：
    • my_list = [
        {
            "id": 1,
            "value": [1, 3, 5, 7]
        },
        {
            "id": 2,
            "value": [2, 4, 6, 8]
        },
        {
            "id": 3,
            "value": [1, 2, 3, 4]
        },
        {
            "id": 4,
            "value": [4, 3, 2, 1]
        }
    ]

    • 遍历显示my_list中元素，将id为偶数的value值进行反转输出，id为奇数的值原样输出。
    • 涉及知识:
    • 1）Flask中模板文件的使用
2）Flask中模板变量的使用
3）Flask中的控制语句(条件判断和for循环)
4）Flask中自定义模板过滤器
'''
from flask import Flask, render_template

app = Flask(__name__)


# 自定义过滤器魔板
@app.template_filter('li_reverse')
def do_li_reverse(li):
    temp = list(li)
    temp.reverse()
    return temp


@app.route('/')
def use_temp():
    my_list = [
        {
            "id": 1,
            "value": [1, 3, 5, 7]
        },
        {
            "id": 2,
            "value": [2, 4, 6, 8]
        },
        {
            "id": 3,
            "value": [1, 2, 3, 4]
        },
        {
            "id": 4,
            "value": [4, 3, 2, 1]
        }
    ]
    return render_template('temp.html', my_list=my_list)


if __name__ == '__main__':
    app.run(debug=True)

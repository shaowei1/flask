from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

'''
re.match 每次执行都编译
a = compile 编译一次，多次使用
a.match()
'''

# 自定义转换器一：代码的扩展性不强，正则表达式为固定的格式，只能匹配4位数值
# class RegexConverter(BaseConverter):
#     regex = '[0-9]{4}'

# 自定义转换器二：代码的扩展性更强，正则表达式是通过函数传参的形式实现，可以任意匹配。
class RegexConverter(BaseConverter):

    def __init__(self, map, *args):
        super(RegexConverter, self).__init__(map)
        print(map)
        '''
        Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>])
        '''
        self.regex = args[0]
        print(args[0])
        # [a-z]{3}


# 把自定义转换器添加到默认转换器字典中
app.url_map.converters['re'] = RegexConverter


@app.route('/<re("[a-z]{3}"):args>')
def index(args):
    return 'hello world %s' % args


if __name__ == '__main__':
    app.run(debug=True)

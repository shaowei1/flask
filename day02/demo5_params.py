from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 给视图传入参数
# 语法：在url中使用<>,本质是使用werkzeug路由模块中的转换器
# 默认是字符串，兼容数值。
# int表示限制数据类型
@app.route('/<int:args>')  # 内置6种转换器string/int/float/any/path/uuid # uuid 全局唯一标识符
def index(args):
    # 接收url中传入的参数，直接返回
    return 'hello world %s' % args


'''
class IntegerConverter(NumberConverter):

    """This converter only accepts integer values::

        Rule('/page/<int:page>')

    This converter does not support negative values.

    :param map: the :class:`Map`.
    :param fixed_digits: the number of fixed digits in the URL.  If you set
                         this to ``4`` for example, the application will
                         only match if the url looks like ``/0001/``.  The
                         default is variable length.
    :param min: the minimal value.
    :param max: the maximal value.
    """
    regex = r'\d+'
    num_convert = int

'''

if __name__ == '__main__':
    print(app.url_map)
    '''
    Map([<Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>,
 <Rule '/<args>' (GET, OPTIONS, HEAD) -> index>])
    '''
    app.run(debug=True)

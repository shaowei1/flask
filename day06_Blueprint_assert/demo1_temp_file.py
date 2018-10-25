from flask import Blueprint

# 1.创建蓝图对象，url_prefix表示url的前缀
# api = Blueprint('api', __name__, url_prefix='/api')  # 使用url_prefix可以帮助确定视图所在位置,这个可以保证在多个蓝图中使用相同的URL规则而不会最终引起冲突
api = Blueprint('api', __name__)

# 把再次拆分的文件，导入到创建蓝图对象的文件中
# 为了避免循环导入，把再次拆分的文件导入到创建蓝图对象的下面
from demo1_goods_orders import goods, orders


# 2. 创建蓝图路由
@api.route('/list')
def list():
    return 'list'


@api.route('/detail')
def detail():
    return 'detail'

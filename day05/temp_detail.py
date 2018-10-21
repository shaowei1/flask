# from demo4_blueprint import app 都导入的话会产生循环导包问题，解决办法切换作用域，不过导包不能解决路由映射问题
# 导入蓝图
from flask import Blueprint

# 1、创建蓝图对象
api = Blueprint('api', __name__)


# 2、使用蓝图对象
@api.route('/detail')
def detail():
    return 'detail'

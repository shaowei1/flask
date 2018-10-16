"""
flask base is a web server
1. import Flask
2. create Flask instance
3. define route mapping and view function, {key: value}
4. start server
"""

# 不适用装饰器，也能实现route mapping
from flask import Flask

# create a instance object:
# import name -> file name -> string.startswith
# __name__, 确认程序所在位置, __name__ == __main__ == 'hello'==abcd==ab
# not 'abc'
# 可以传入任意字符串 ->
# 如果传入标准模块名，会导致程序instance path 创建不成功，只会影响static file 访问
# (os 如果不是标准模块os会从当前路径下查找)
# flask 会默认创建静态文件的访问路径，方便静态文件的访问
# 1. 不能不传入参数,不能传入数值，可以传入任意字符串
# 2. 如果传入标准模块名，会导致程序实例路径instance_path创建不成功
# 3. 只会影响静态文件的访问，不会影响视图函数的访问

# Conclusion
# 视图函数名不能重复(因为函数名重复，相当于一个路径两个返回值)
# url可以重复(因为不同的请求方法，对后端代码不同的操作,get(see),post(add),put(modify),delete(delete)
# 执行顺序从上到下，依次查找，如果找到，不会继续往下查找
# url 匹配首先匹配的路径，其次匹配http请求方法

app = Flask(__name__)
'''
def __init__(self, import_name, static_path=None, static_url_path=None,
                 static_folder='static', template_folder='templates',
                 instance_path=None, instance_relative_config=False,
                 root_path=None):
                 
import_name
# Flask 程序所在的包(module), __name__
# 其可以决定Flask_path在访问静态文件时查找的路径
static_path
# 静态文件访问路径(no recommend use, replace by static_url_path)
static_url_path
# 静态文件访问路径，可以不传，默认为：/ + static_folder
template_folder
模板文件存储的文件夹，可以不传，默认为 templates
'''


# default of methods contain GET, OPTIONS, HEAD
@app.route('/', methods=['POST'])
def hello2019():
    a = 1
    b = 2
    return a, b


'''

def route(self, rule, **options):
    """A decorator that is used to register a view function for a
    given URL rule.  This does the same thing as :meth:`add_url_rule`
    but is intended for decorator usage::

    def decorator(f):
        endpoint = options.pop('endpoint', None)
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator

self.add_url_rule(self.static_url_path + '/<path:filename>',
                              endpoint='static',
                              view_func=self.send_static_file)
'''


# @app.route('/')
def hello():
    return 'hello world'


# 手动添加路由映射，不适用装饰器
# params: rule, endpoint, view function name
app.add_url_rule('/', 'hello', hello)

# 当前文件独立运行,__name__=='__main__'
# 当被其他文件导入, __name__=='hello'
if __name__ == '__main__':
    # see all route mapping
    print(app.url_map)
    # < 存对象
    # Map[<Rule '/' (HEAD, GET, OPTIONS) -> hello>,
    # <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>])
    # debut调试模式，自动跟踪代码的变化,只有在开发模式下开启，定位bug position
    # 生产模式下不能开启调试模式
    app.run(debug=True)

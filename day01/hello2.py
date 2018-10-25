from flask import Flask

"""
flask基本程序的实现:本质是web服务器
1、导入Flask类
2、创建Flask类的实例对象
3、定义路由映射以及视图函数，{key:value}
4、启动服务器

hello_2018

"""
# 创建类的实例对象：
# __name__参数的作用：确认程序所在的位置；Flask会默认创建静态文件的访问路径，方便静态文件的访问。
# 1、不能不传参数、不能传入数值,可以传入任意字符串
# 2、如果传入标准模块名，会导致程序实例路径instance_path创建不成功，
# 3、只会影响静态文件的访问，不会影响视图函数的访问
app = Flask(__name__,  # __name__代表app对象所在模块名，模块目录决定了查找模板文件和静态文件的目录
            static_folder='static',  # 静态文件保存的目录，默认值:static
            static_url_path='/static',  # 设置访问静态文件url路径的前缀，默认值:/static
            template_folder='templates',  # 模板文件保存的目录，默认值:templates
            )


class Config(object):
    """配置类"""
    DEBUG = True


# 加载项目配置信息
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'hello world2018'


from flask import redirect


@app.route('/redirect')
def demo5():
    return redirect('http://www.baidu.com')


# 手动添加路由映射，不使用装饰器；
# 第一个参数表示url规则rule，第二个参数端点endpoint，第三个参数是视图函数名
# app.add_url_rule('/','hello',hello)


# 当前文件独立运行的时候，该表达式成立
# 当前文件被其它文件导入使用的时候，该表达式不成立，__name__ == 'hello'
if __name__ == '__main__':
    # 查看程序所有的路由映射
    print(app.url_map)
    # debug调试模式：自动跟踪代码的变化，只有在开发模式开启,方便定位代码bug所在的位置。
    # 生产模式下不能开启调试模式
    app.run(port=5001, debug=True)

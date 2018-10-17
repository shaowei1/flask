"""
1. import Flask
2. create Flask instance
3. define route mapping and view function, {key: value}
4. start server
"""

# 不适用装饰器，也能实现route mapping
from flask import Flask

# import name -> file name -> string.startswith
# __name__, 确认程序所在位置, __name__ == __main__ == 'hello'==abcd==ab
# not 'abc'
# 可以传入任意字符串 ->
# 如果传入标准模块名，会导致程序instance path 创建不成功，只会影响static file 访问

# flask 会默认创建静态文件的访问路径，方便静态文件的访问
app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello world'


# rule, endpoint, view function name
# app.add_url_rule('/', 'hello', hello)

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
    # app.run(debug=True)
    app.run()

from flask import Flask
# 导入flask_script扩展包
from flask_script import Manager

app = Flask(__name__)

# app.config['DEBUG'] = True

# 实例化管理器对象,让管理器对象和程序实例进行关联
manage = Manager(app)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    # app.run(debug=True,host=,port=5005)
    # 作用：
    # 1、可以在终端以命令的形式传入参数，手动指定ip和port
    # 2、后面配置flask_migrate扩展实现数据库的迁移。

    manage.run()
'''
python3 demo2_script.py runserver -h 0.0.0.0
-h  HOST
-p  PORT
-d  --debug
-D  --no-debug
-r  --reload
-R  --no-reload
'''

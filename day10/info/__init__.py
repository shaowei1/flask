from flask import Flask
# 导入配置类
from config import Config,config_dict
# 导入Flask_session
from flask_session import Session
# 导入flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# 导入标准日志模块
import logging
from logging.handlers import RotatingFileHandler
# 导入redis模块
from redis import StrictRedis

# 实例化redis连接对象,需要存储和业务相关的数据比如图片验证码。
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT,decode_responses=True)


# 实例化sqlalchemy对象
db = SQLAlchemy()



# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG) # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)



# 定义工厂函数：用来接收参数，来根据参数的不同，生产不同环境下的app
# config_name=='development' debug = True
# config_name=='production' debug = False
def create_app(config_name):
    app = Flask(__name__)

    # 使用配置对象
    app.config.from_object(config_dict[config_name])

    # 使用Session
    Session(app)
    # 通过函数调用，让db和程序实例进行关联
    db.init_app(app)

    # 导入蓝图对象，注册蓝图
    from info.modules.news import news_blue
    app.register_blueprint(news_blue)
    from info.modules.passport import passport_blue
    app.register_blueprint(passport_blue)

    return app


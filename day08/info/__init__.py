from flask import Flask

from config import Config, config_dict

from flask_session import Session

from flask_sqlalchemy import SQLAlchemy

import logging

from logging.handlers import RotatingFileHandler

from redis import StrictRedis

# instantiation object of redis connect, that need to save data about business, such as picture verification code
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)

# instantiation sqlalchemy object
db = SQLAlchemy()

# setting record level of log
logging.basicConfig(level=logging.DEBUG)  # debugging debug level

# Create logger for set path of log saving, one log file max size 100M, max numbers of log files
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
# create format of log file, content log level , filename, row number, log information
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# use format
file_log_handler.setFormatter(formatter)
# add logger for log tool object of global (flask app)
logging.getLogger().addHandler(file_log_handler)


# defined factory function: accept params, with different params make different environment's app
# config_name=='development' debug = True
# config_name=='production' debug = False
def create_app(config_name):
    app = Flask(__name__)

    # use config object
    app.config.from_object(config_dict[config_name])

    Session(app)

    # adopt function call , make relative in db and instance of programing
    db.init_app(app)

    # import blueprint object, register blueprint
    from info.modules.news import news_blue
    app.register_blueprint(news_blue)
    from info.modules.passport import possport_blue
    app.register_blueprint(possport_blue)

    return app


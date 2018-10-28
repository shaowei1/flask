from redis import StrictRedis


class Config:
    # debug information
    DEBUG = None
    SECRET_KEY = 'QPMe4qEs9pHF3+95LadkcO5iPNhZw+QXvDpHz5o3dIHLQUwZ1IKEiEsjMBS5T7Kbd/IXv4AEU2HwZ48sb/AREg=='
    SQLALCHEMY_DATABASE_URI = 'mysql://demouser:demopassword@127.0.0.1/info'
    # Dynamic track repair , if not will get a warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, post=REDIS_PORT)
    SESSION_USER_SIGNER = True  # SESSION information signature
    PERMANENT_SESSION_LIFETIME = 86400  # flask self's session Term of validity


# define config of development models
class DevelopmentConfig(Config):
    DEBUG = True


# define config of production models
class ProductionConfig(Config):
    DEBUG = False


# defined dictionary mapping config class of different environment
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}

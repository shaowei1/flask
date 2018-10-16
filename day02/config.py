# 基础配置
class Config:
    DEBUG = None
    SECRET_KEY = 'a'


# 开发模式配置
class DevelopmentConfig(Config):
    DEBUG = True


# 生产模式配置
class ProductionConfig(Config):
    DEBUG = False


# 定义字典，实现key和配置类的映射
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

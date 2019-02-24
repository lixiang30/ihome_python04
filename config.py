import redis
import pymysql

class Config(object):
    """配置信息"""
    DEBUG = True
    SECRET_KEY = "HHDBE*YSFDHHJ"
    # 数据库
    # SQLALCHEMY_DATABASE_URI = "mysql://root:huang921118@127.0.01:3306/ihome_python04"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:huang921118@127.0.0.1/ihome_python04"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_PASSWORD = "plmokn10241118"
    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USER_SIGNER = True # 对cookie中的session进行隐藏
    PERMANENT_SESSION_LIFETIME = 86400 # session数据的有效期,单位秒

class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True

class ProductionConfig(Config):
    """生产环境配置信息"""
    pass

config_map = {
    "develop":DevelopmentConfig,
    "product":ProductionConfig,
}
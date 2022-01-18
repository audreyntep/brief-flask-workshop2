class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "audreyntep2022"

    DB_NAME = 'production.db'

    UPLOADS = "/" # path to uploads directory

    SESSION_COOKIE_NAME = 'myapp'
    SESSION_COOKIE_SECURE = True

    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = 'development.db'
    
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    DB_NAME = 'development.db'
class Config:
    SECRET_KEY = 'hard to guess string'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'namthongminhghe@gmail.com'
    MAIL_PASSWORD = 'vgkuuykzkfftvuwi'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'namthongminhghe@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/user'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/user'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/user'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

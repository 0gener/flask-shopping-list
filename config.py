class Config:
    TESTING = False
    DEBUG = False
    PROPAGATE_EXCEPTIONS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'

class DevelopmentConfig(Config):
    TESTING = False
    DEBUG = True

class StagingConfig(Config):
    TESTING = False
    DEBUG = True

class ProductionConfig(Config):
    TESTING = False
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
from os import environ

class Config:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = False
    DEBUG = False
    SECRET_KEY = environ.get('SECRET_KEY')
    PROPAGATE_EXCEPTIONS = environ.get('PROPAGATE_EXCEPTIONS')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")

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
}
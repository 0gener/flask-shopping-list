from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import app_config

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile('config.py')
    app.config.from_object(app_config[config])

    from application.api.resources import api
    api.init_app(app)

    jwt.init_app(app)
    db.init_app(app)

    return app
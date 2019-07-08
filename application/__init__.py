from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import app_config

api = Api()
db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)

    app.config.from_object(app_config[config])

    db.init_app(app)
    api.init_app(app)

    return app
from flask_restful import Api

from .user import UserRegister, UserLogin

api = Api()
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
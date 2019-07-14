from flask_restful import Api

from .user.user import UserRegister, UserLogin, TokenRefresh

api = Api()
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/token/refresh')
from flask_restful import Api

from .user.user import UserRegister, UserLogin, TokenRefresh
from .group.group import Group
from .item.item import Item

api = Api()
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/token/refresh')
api.add_resource(Group, '/group')
api.add_resource(Item, '/group/<int:group_id>/item')
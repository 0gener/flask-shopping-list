from flask import request
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from application.rdb.models.user import UserModel
from flask_jwt_extended import (
    jwt_refresh_token_required,
    get_jwt_identity
)
from .models.user_register_request import UserRegisterRequest
from .models.user_login_request import UserLoginRequest
from application.rdb.models.user_session import create_login_session, create_refresh_session

class UserRegister(Resource):
    @staticmethod
    def post():
        req = UserRegisterRequest(request.get_json())

        if UserModel.find_by_username(req.username):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(req.username, req.password, req.first_name, req.last_name, req.email)
        user.save()

        return {"message": "User created successfully."}, 201

class UserLogin(Resource):
    @staticmethod
    def post():
        req = UserLoginRequest(request.get_json())

        user = UserModel.find_by_username(req.username)

        if user and safe_str_cmp(user.password, req.password):
            session = create_login_session(user.id)

            return session.json(), 200

        return {"message": "Invalid credentials"}, 401

    @staticmethod
    def __get_time_in_seconds(time):
        if isinstance(time, int):
            return time
        else:
            return time.total_seconds()


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user_id = get_jwt_identity()

        session = create_refresh_session(current_user_id)

        return session.json(), 200

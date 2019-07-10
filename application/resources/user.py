from flask import current_app
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from application.models.user import UserModel
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)

class UserRegister(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('username',
            type=str,
            required=True,
            help="This field cannot be blank."
        )
        parser.add_argument('password',
            type=str,
            required=True,
            help="This field cannot be blank."
        )
        parser.add_argument('first_name',
            type=str,
            required=True,
            help="This field cannot be blank."
        )
        parser.add_argument('last_name',
            type=str,
            required=True,
            help="This field cannot be blank."
        )
        parser.add_argument('email',
            type=str,
            required=True,
            help="This field cannot be blank."
        )

        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data.username, data.password, data.first_name, data.last_name, data.email)
        user.save()

        return {"message": "User created successfully."}, 201

class UserLogin(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('username',
            type=str,
            required=True,
            help="This field cannot be blank."
        )
        parser.add_argument('password',
            type=str,
            required=True,
            help="This field cannot be blank."
        )

        data = parser.parse_args()

        user = UserModel.find_by_username(data.username)

        if user and safe_str_cmp(user.password, data.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)

            access_token_expiration = current_app.config['JWT_ACCESS_TOKEN_EXPIRES'].total_seconds()
            refresh_token_expiration = current_app.config['JWT_REFRESH_TOKEN_EXPIRES'].total_seconds()

            return {
                "access_token": access_token,
                "expires_in": access_token_expiration,
                "refresh_token": refresh_token,
                "refresh_expires_in": refresh_token_expiration
            }, 200

        return {"message": "Invalid credentials"}, 401
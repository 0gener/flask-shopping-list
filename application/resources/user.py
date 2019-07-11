from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from application.models.user import UserModel
from flask_jwt_extended import (
    jwt_refresh_token_required,
    get_jwt_identity
)
from application.models.user_session import create_login_session, create_refresh_session

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

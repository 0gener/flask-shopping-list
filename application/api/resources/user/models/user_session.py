from flask import current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)

def create_login_session(_id):
    return __create_session(_id, True)

def create_refresh_session(_id):
    return __create_session(_id, False)

def __create_session(_id, fresh):
    access_token = create_access_token(identity=_id, fresh=fresh)
    refresh_token = create_refresh_token(_id)

    access_token_expiration = __get_time_in_seconds(current_app.config['JWT_ACCESS_TOKEN_EXPIRES'])
    refresh_token_expiration = __get_time_in_seconds(current_app.config['JWT_REFRESH_TOKEN_EXPIRES'])

    return UserSession(access_token, access_token_expiration, refresh_token, refresh_token_expiration)

def __get_time_in_seconds(time):
    if isinstance(time, int):
        return time
    else:
        return time.total_seconds()

class UserSession:
    def __init__(self, access_token, expires_in, refresh_token, refresh_expires_in):
        self.access_token = access_token
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.refresh_expires_in = refresh_expires_in

    def json(self):
        return {
            'access_token': self.access_token,
            'expires_in': self.expires_in,
            'refresh_token': self.refresh_token,
            'refresh_expires_in': self.refresh_expires_in
        }
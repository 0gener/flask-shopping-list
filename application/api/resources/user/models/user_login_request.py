from application.api.resources.common.common_request import CommonRequest

class UserLoginRequest(CommonRequest):
    def __init__(self, request: dict):
        self.username = super().load_field(request, 'username')
        self.password = super().load_field(request, 'password')

    def validate(self):
        if self.username is None or self.password is None:
            raise Exception()
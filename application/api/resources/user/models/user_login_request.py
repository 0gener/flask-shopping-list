from application.api.resources.common.common_request import CommonRequest

class UserLoginRequest(CommonRequest):
    def __init__(self, request: dict):
        super().__init__(request)

        self.username = self.load_field('username')
        self.password = self.load_field('password')

    def validate(self):
        if self.username is None or self.password is None:
            raise Exception()
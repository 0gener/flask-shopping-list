from application.api.resources.common.common_request import CommonRequest

class UserRegisterRequest(CommonRequest):
    def __init__(self, request: dict):
        super().__init__(request)

        self.username = self.load_field('username')
        self.password = self.load_field('password')
        self.first_name = self.load_field('first_name')
        self.last_name = self.load_field('last_name')
        self.email = self.load_field('email')

    def validate(self):
        if self.username is None or self.password is None or self.first_name is None or self.last_name is None or self.email is None:
            raise Exception
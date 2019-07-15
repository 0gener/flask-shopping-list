from application.api.resources.common.common_request import CommonRequest

class UserRegisterRequest(CommonRequest):
    def __init__(self, request: dict):
        self.username = super().load_field(request, 'username')
        self.password = super().load_field(request, 'password')
        self.first_name = super().load_field(request, 'first_name')
        self.last_name = super().load_field(request, 'last_name')
        self.email = super().load_field(request, 'email')

    def validate(self):
        if self.username is None or self.password is None or self.first_name is None or self.last_name is None or self.email is None:
            raise Exception
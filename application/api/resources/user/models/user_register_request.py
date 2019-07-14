class UserRegisterRequest:
    def __init__(self, request:dict):
        self.username = request['username']
        self.password = request['password']
        self.first_name = request['first_name']
        self.last_name = request['last_name']
        self.email = request['email']
from application.api.resources.common.common_request import CommonRequest

class CreateGroupRequest(CommonRequest):
    def __init__(self, request: dict):
        super().__init__(request)

        self.name = self.load_field('name')

    def validate(self):
        if self.name is None:
            raise Exception()
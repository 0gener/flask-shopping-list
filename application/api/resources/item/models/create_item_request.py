from application.api.resources.common.common_request import CommonRequest

class CreateItemRequest(CommonRequest):
    def __init__(self, request: dict):
        self.name = super().load_field(request, 'name')

    def validate(self):
        if self.name is None:
            raise Exception()
class CommonRequest:
    def __init__(self, request: dict):
        self.request = request

    def load_field(self, field:str):
        try:
            return self.request[field]
        except:
            return None
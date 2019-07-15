class CommonRequest:
    @staticmethod
    def load_field(request:dict, field:str):
        try:
            return request[field]
        except:
            return None
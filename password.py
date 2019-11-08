class User:
    users = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    pass

class Credentials:
    credential_list = []
    
    def __init__(self, account_name, password):
        self.account_name = account_name
        self.password = password
    pass

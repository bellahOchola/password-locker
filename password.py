class User:
    users_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def create_account(self):
        User.users_list.append(self)

    @classmethod
    def login(cls,user_name, password):
        '''
        this method takes in the username and password of user and enables them to login
        '''

        for user in cls.users_list:
            if user.user_name == user_name and user.password == password:
                return True

        return False

class Credentials:
    credential_list = []
    
    def __init__(self, account_name, password):
        self.account_name = account_name
        self.password = password
    
    def create_credentials(self):
        Credentials.credential_list.append(self)

    

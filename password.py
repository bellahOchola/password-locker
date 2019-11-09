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
    
    def save_credential(self):
        Credentials.credential_list.append(self)

    def delete_credential(self):
        Credentials.credential_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method returns the credentials list
        '''
        return cls.credential_list

    @classmethod
    def find_by_accountname(cls,account_name):
        '''
        this method returns the password of the account entered
        '''
        for credentials in cls.credential_list:
            if credentials.account_name == account_name :
                return credentials
        


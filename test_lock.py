import unittest
from password import *

class TestUser(unittest.TestCase):
    '''
    This is a test class that defines test cases 
    for user login and signup details.
    Args:
        unittest.TestCase: TestCase class aids in the formation of test cases
    '''

    def setUp(self):
        '''
        method to run before each test case.
        '''
        self.new_user = User('ocholaB','ochola@1990')

    def tearDown(self):
        '''
        method that is run after each test case
        '''
        User.users_list = []
    
    def test_init(self):
        '''
        tests if the object is initialized in the right way
        '''
        self.assertEqual(self.new_user.user_name,'ocholaB')
        self.assertEqual(self.new_user.password,'ochola@1990')

    def test_create_account(self):
        '''
        tests that enables user sign up to the application
        '''
        self.new_user.create_account()
        self.assertEqual(len(User.users_list),1)

    def test_save_multiple_accounts(self):
        '''
        checks if we can store multiple accounts 
        '''
        self.new_user.create_account()
        user1 = User('kamau', 'kamau123')
        user1.create_account()
        self.assertEqual(len(User.users_list),2)

    def test_user_existance(self):
        '''
        checks if the user details already exist by using their username and passwords
        '''
        self.new_user.create_account()
        user1 = User('kamau', 'kamau123')
        user1.create_account()
        find_user = User.login('kamau','kamau123')
        self.assertTrue(find_user)

class TestCredentials(unittest.TestCase):
    '''
    class that enables user view their credentials, delete and even create new ones
    '''
    def setUp(self):
        '''
        method to run before each test case.
        '''
        self.new_credentials = Credentials('twitter','twit346')

    def tearDown(self):
        '''
        method to run after each test case.
        '''
        Credentials.credential_list= []


    def test_init(self):
        '''
        tests if the object is initialized in the right way
        '''
        self.assertEqual(self.new_credentials.account_name,'twitter')
        self.assertEqual(self.new_credentials.user_name,'bellah')
        self.assertEqual(self.new_credentials.password,'twit346')

    def test_create_credentials(self):
        '''
        this test enables user to create new account credentials
        '''
        self.new_credentials.create_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_save_multiple_credentials(self):
        '''
        test that enables user store multiple account credentials
        '''
        self.new_credentials.create_credentials()
        user1 = Credentials('facebook','john', 'fbv35')
        user1.create_credentials()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_find_credential(self):
        '''
        test enables user find the password of a specific account
        '''
        self.new_credentials.create_credentials()
        user1 = Credentials('facebook', 'john',fbv35')
        user1.create_credentials()
        find_credential = Credentials.find_by_accountname('facebook')
        self.assertEqual(find_credential.password,user1.password)

    def test_display_credential(self):
        '''
        this test enables user view their account credentials
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)

    def test_delete_credential(self):
        '''
        test allows user delete a given accounts credentials
        '''
        self.new_credentials.create_credentials()
        self.new_credentials.delete_credential()
        self.assertEqual(len(Credentials.credential_list),0)

if __name__ == '__main__':
    unittest.main()

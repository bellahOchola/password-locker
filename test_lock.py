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
        User.users = []
    
    def test_init(self):
        '''
        tests if the object is initialized in the right way
        '''
        self.assertEqual(self.new_user.user_name,'ocholaB')
        self.assertEqual(self.new_user.password,'ochola@1990')

    def test_create_account(self):
        '''
        tests 
        '''
        self.new_user.create_account()
        self.assertEqual(len(User.users),1)
        

if __name__ == '__main__':
    unittest.main()

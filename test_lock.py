import unittest
from password import User

class TestUser(unittest.Testcase):
    '''
    This is a test class that defines test cases 
for user login and signup details.
    Args:
        unittest.TestCase: TestCase class aids in the formation of test cases
    '''

    def setUp(self):
        '''
        method to run before each test case.
        ''''
        self.new_user = User('ocholaB','ochola@1990') 
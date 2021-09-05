from user import User  # imported User class from user module
import unittest        # imported in-built unnitest module

class TestUser(unittest.TestCase): 
    '''      
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before the test case
        '''
        self.new_user = User("Jamal", "jayhamo22@gmail.com", "sicario2793")

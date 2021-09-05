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
  
    def tearDown(self):
        '''
        tearDown method  cleans up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test if object utilizes proper instantiation
        '''
        self.assertEqual(self.new_user.user_name,"Jamal")
        self.assertEqual(self.new_user.password,"sicario2793")
        self.assertEqual(self.new_user.email,"jayhamo22@gmail.com")
       
    def test_save_user(self):
        '''
         tests if the user object is saved in users array
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list), 1)
    

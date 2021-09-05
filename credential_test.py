from credential import Credential  # Importing Credential Class from credential module
import unittest                    # Importing an inbuilt unittest Module for unit testing

class TestCredential(unittest.TestCase):
          
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Jamal", "Hassan", "Jamal", "sicario2793", "jayhamo22@gmail.com") 

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.first_name, "Jamal")
        self.assertEqual(self.new_credential.last_name, "Hassan")
        self.assertEqual(self.new_credential.user_name, "Jamal")
        self.assertEqual(self.new_credential.password, "sicario2793")
        self.assertEqual(self.new_credential.email, "jayhamo22@gmail.com")

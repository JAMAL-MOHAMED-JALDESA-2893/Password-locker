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


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []


    def test_save_credential(self):
        '''
        Test if credential object is saved in credential_list
        '''
        self.new_credential.save_credential() 
        self.assertEqual(len(Credential.credential_list), 1)

     
    def test_delete_credential(self):
        '''
        this method tests if we can remove a credential from our credentials_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Jamal", "Hassn", "Jamal", "sicario2793", "jayhamo22@gmail.com")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)


    def test_find_credentials_by_email(self):
        '''
        test to check if we can find a credentials by email and display information
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Jamal", "Hassan", "Jamal", "sicario2793", "jayhamo22@gmail.com")
        test_credential.save_credential()
        found_credential = Credential.find_email("jayhamo22@gmail.com")
        self.assertEqual(found_credential.first_name, test_credential.first_name)



    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the credentials
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Jamal", "Hassan", "", "sicario2793", "jayhamo22@gmail.com")
        test_credential.save_credential()
        credentials_exists = Credential.credential_exit("jayhamo22@gmail.com")
        self.assertTrue(credentials_exists)  


    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credential.display_credential(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()       
 
import unittest #Importing from unittest module
from user import User #importing user details
from credentials import Credentials #importing credientials details

class TestUser(unittest.TestCase):
    """"
    Test class that defines test cases for the user class behaviours
    
    Args: unittest.Testcase: TestCase class that helps in creating test cases
    """
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has been run
        """
        User.user_list = []

    def setUp(self):
        """
        Set up method to run before each test case
        """
        self.new_user = User("Fawz", "6720") #created new user

    def test_init(self):
        """test_init case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, "Fawz")
        self.assertEqual(self.new_user.password, "6720")

    def test_save_user(self):
        """test_save_user test to test if we are able to save the users details
        """
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        """
        test_delete_user test to test if we are able delete our user
        """
        self.new_user.save_user()
        test_user = User("Fawz", "6720")
        test_user.save_user()

        self.new_user.delete_user() # to delete a user
        self.assertEqual(len(User.user_list), 1)

    def test_display_user(self):
        '''
        method that returns a list of all contacts saved
        '''
        self.assertEqual(User.display_name(),User.user_list)

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credentials class behaviours
    
    Args:
    Unittest.Testcase. Testcase class that helps in creating test cases
    """

    def tearDown(self):
        """
        TearDown cleans up after each test case
        """
        Credentials.credentials_list = []

    def setUp(self):
         """
         SetUp method to run before each test cases
         """
         self.new_cred = Credentials("instagram", "2020") #created new credentials and password

    def test_save_credentials(self):
        """"
    test_save_credentials test case to test if the credentials object is saved to the credentials list
    """
        self.new_cred.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a cred from our cred list
            '''
            self.new_cred.save_credentials()
            test_cred = Credentials("Instagram","2020")
            test_cred.save_credentials()

            self.new_cred.delete_credentials()
            self.assertEqual(len(Credentials.credentials_list),1)
            
    def test_display_credentials(self):
            '''
        method that returns a list of all credentials saved
        '''

            self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()
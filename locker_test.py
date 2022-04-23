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




if __name__ == '__main__':
    unittest.main()
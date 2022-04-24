class Credentials:

    """
    A class that generates new instances of our password 
    """
    credentials_list = []

    def __init__(self, account_name, account_password):
        """
        A method that defines properties of the credentials class
        """
        self.account_name = account_name
        self.account_password = account_password

    def save_credentials(self):
        """
        method that saves the credentials of the user 
        """
        Credentials.credentials_list.append(self)

    def d




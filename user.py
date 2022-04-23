class User:
    """
    Class that generates new instances of the users
    """
    user_list = [] #empty user-list

    def __init__(self, username, password):
        """
        A method that defines properties of the User class
        """

        self.username = username
        self.password = password
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

    def save_user(self):
        """
        method to save a new user into user_list
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        method to delete a new user form the user_list
        """
        User.user_list.remove(self)


#!usr/bin/env python3.8
from user import User
from credentials import Credentials
import random

def create_user(username, password):
    """
    Function  that create new user
    """
    new_user = User(username, password)
    return new_user

def save_user(user):
    """"
    function that saves a user
    """
    user.save_user()

def delete_user(user):
    """
    Function that deletes a user
    """
    user.delete_user()

de

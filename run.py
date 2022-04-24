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

def create_credentials(account_name, account_password):
    """
    Function to create new credentials
    """
    new_cred = Credentials(account_name, account_password)
    return new_cred

def save_credentials(credentials):
    """
    function that saves new credentials
    """
    credentials.save_credentials()

def delete_credentials(credentials):
    """
    function that deletes credentials
    """
    credentials.delete_credentials()

def get_credentials(account_name):
    """
    Function that finds a credential and returns it
    """
    return Credentials.get_credentials(account_name)

def display_credentials():
    """
    function that returns saved credentials
    """

    return Credentials.display_credentials()
#!/usr/bin/env python3.8
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


def main():
    print("Hello, Welcome to password locker. What is your name?")
    name = input()
    print(f"Nice to meet you {name}. \n")
    print("Pls use the following short codes to navigate through the application; ")
    print("na -To create a new account.")
    print("lg -To log in to your account.")
    short_code = input("Select a short code: ")
    print("\n")

    while True:
         
#Create a new account to Password locker

        if short_code == "na":
            print("To create a new account, you have to create a username and a new password")
            print("Input a Username:")
            username = input()
            print("Create a new password:")
            password = input()
            save_user(create_user(username, password))
            print("Can you please confirm your password")
            confirm_password = input()

#if the passwords do not match

            while confirm_password != password:
                print("Your passwords do not match")
                print("\n")
                print("Create your password again")
                password = input()
                print("Confirm password")
                confirm_password = input()

            else: 
                print("\n")
                print(f"Welcome {username}. You have successfully created a Password account. \n")
                print("Enter your login details to continue...")
                print("Enter Username")
                login_username = input()
                print("Enter login password")
                login_password = input()

#if the login details do not match the account created logins

            while username != login_username != login_password != password:
                print("\n")
                print("Your username and login details do not math. Please try again")
                print("Enter Username")
                login_username = input()
                print("Enter login password")
                login_password = input()

            else:
                print("\n")
                print(f"Welcome {username} to your password locker.")
                print("You can be able to interact with your passwords here.")

#Log In if you already have an account

        elif short_code == "lg":
            



                







if __name__ == '__main__':

        main()

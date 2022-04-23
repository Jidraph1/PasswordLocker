import random
#random values generator form a given range

characters = "abcdefghijklmnopqrstuvwxABCDEFGHIJKLMNOPQRSTUVWXYZ" #The character range for the password

while 1: #While 1 is an infinite loop, meaning it will run all through the code
    pass_len = int(input("How long would you like your new password to be? We suggest a long password for security purposes: \n")) 
    pass_count = int(input("How many passwords would you like generated? \n"))

    for i in range(0,pass_count):
        password = ""
        for i in range(0,pass_len): 
            password_characters = random.choice(characters)
            password = password_characters
            print("Well Done, here is your new password: \n", password)
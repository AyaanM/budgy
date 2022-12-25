'''
title: Start Up Page (to login & register)
author: Ayaan Merchant
date-created: 2022-12-24
'''

import functions, databases
from os import remove

def start():
    USER_TYPE = input("Welcome to Budgy! \n Are You a Returning User (r) Or a New User (n), (type r or n) > ")
    if USER_TYPE == "R" or USER_TYPE == "r":
        pass
    elif USER_TYPE == "N" or USER_TYPE == "n":
        register()
    else:
        print("Command Not Understood, Please Try Again")
        start()

def register():
    USERNAME = input("Your Name: ")

    PASSWORD1 = input("New Password: ")
    CONFIRM_PASS = input("Confirm Password: ")
    if functions.checkSamePass(PASSWORD1, CONFIRM_PASS) == True:
        PASSWORD = PASSWORD1
    else:
        print("You Took Too Many Tries, Please Try Again Later.")
        remove("user_account.db") # if took too many tries, user has to wait before creating account
        exit()

    BALANCE_CHECKING = functions.checkInt(input("Your Checking Account's Balance (this can be updated later): "))
    BALANCE_SAVINGS = functions.checkInt(input("Your Saving Account's Balance (this can be updated later): "))

    INFO = [USERNAME, PASSWORD, BALANCE_CHECKING, BALANCE_SAVINGS]
    USER = databases.user_database # make the user DB
    USER.createAccount(INFO) # add user info to the user DB

    MAIN.addAccounts(USERNAME, PASSWORD) # add newly created account to file
    print("Account Creation Successful")


if __name__ == "__main__":
    MAIN = databases.mainDB
    
    start()

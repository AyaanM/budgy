'''
file where all the processes considering user databases will take place (done to unclutter main user file)
author: Ayaan Merchant
date-created: 2022-11-16
'''

import sqlite3
import functions
from os import remove


class user_database:
    def __init__(self):
        self.CONNECTION = sqlite3.connect("user_account.db") #connect to the users account
        self.CURSOR = self.CONNECTION.cursor()
        self.USERNAME = ""
        self.PASSWORD = ""
        self.BALANCE_CHECKING = None
        self.BALANCE_SAVINGS = None

    def createAccount(self): # create database to store user account and get info

        self.CURSOR.execute('''
            CREATE TABLE
                user_account(
                    username TEXT NOT NULL PRIMARY KEY,
                    password TEXT NOT NULL,
                    balance_checking INT NOT NULL,
                    balance_saving INT NOT NULL
                )
        ;''')

        self.CURSOR.execute('''
        CREATE TABLE
            user_transactions(
                transaction_amount INT NOT NULL,
                transaction_location TEXT NOT NULL,
                transaction_date TEXT NOT NULL,
                transaction_type TEXT NOT NULL,
                transaction_account TEXT NOT NULL
            )
    ;''')

        ## import user info into account
        self.USERNAME = input("Your Name: ")

        PASSWORD = input("New Password: ")
        CONFIRM_PASS = input("Confirm Password: ")
        if functions.checkSamePass(PASSWORD, CONFIRM_PASS) == True:
            self.PASSWORD = PASSWORD
        else:
            print("You Took Too Many Tries, Please Try Again Later.")
            remove("user_account.db") # if took too many tries, user has to wait before creating account
            exit()

        self.BALANCE_CHECKING = functions.checkInt(input("Your Checking Account's Balance (this can be updated later): "))
        self.BALANCE_SAVINGS = functions.checkInt(input("Your Saving Account's Balance (this can be updated later): "))

        INFO = [self.USERNAME, self.PASSWORD, self.BALANCE_CHECKING, self.BALANCE_SAVINGS]

        self.CURSOR.execute('''
            INSERT INTO user_account(username, password, balance_checking, balance_saving)
            VALUES(?, ?, ?, ?)
        ;''', INFO)

    def get_info(self): #get info from DB
        ACCOUNT_DATA = self.CURSOR.execute('''
        SELECT * FROM user_account
        ;''').fetchone()

        ACCOUNT_TRANSACTIONS = self.CURSOR.execute('''
        SELECT * FROM user_transactions
        ;''').fetchall()

        return ACCOUNT_DATA, ACCOUNT_TRANSACTIONS

    def storeData(self, USER_INFO, ACCOUNTS_BALANCE, TRANSACTIONS): # stores user data upon exit

        ACCOUNT_INFO = USER_INFO + ACCOUNTS_BALANCE #username, pass, checkings, savings

        self.CURSOR.execute('''
        UPDATE
            user_account
        SET
            username = ?, 
            password = ?, 
            balance_checking = ?, 
            balance_saving = ?
    ;''', ACCOUNT_INFO)

        for i in range(len(TRANSACTIONS)): # insert each new transaction one by one
            self.CURSOR.execute('''
            INSERT INTO
                user_transactions
            VALUES(
                ?, ?, ?, ?, ?
            )
        ;''', TRANSACTIONS[i]) # amount, location, date, type, account

        self.CONNECTION.commit()


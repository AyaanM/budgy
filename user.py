'''
title: class to see account
author: Ayaan Merchant
date-created: 2022-01-07
'''

import sqlite3
import pathlib
import money
from datetime import date
from time import sleep

### VARIABLES ###
DB_FILE = "user_account.db"
FIRST_RUN = True

if (pathlib.Path.cwd() / DB_FILE).exists():
    FIRST_RUN = False # don't create DB if already created

CONNECTION = sqlite3.connect(DB_FILE)
CURSOR = CONNECTION.cursor()


def checkInt(NUM):
    try:
        NUM = float(NUM)
        return NUM
    except ValueError:
        NEW_NUM = input("Input must be a number: ")
        return checkInt(NEW_NUM)

## create database and do account set up
def createDatabase():
    '''
    create the database for use account
    :return: None
    '''

    CURSOR.execute('''
        CREATE TABLE
            user_account(
                username TEXT PRIMARY KEY,
                account_balance INT,
                transactions TEXT
                )
        ;''') # transactions stores lists converted to strings

def getUserInfo():
    '''
    when first run, get and store user info in DB
    :return: None
    '''
    print("Thank-you for choosing Budgy")
    print("Since this is your first time using Budgy, we will have to set up your account \n")

    NAME = input("Your Name (this will be the same as your username): ")
    CURRENT_BALANCE = checkInt(input("Your Current Account Balance (this can be updated later): "))
    print("Thank-you! Your account has been set up!")

    FIRST_TIME_INFO = (NAME, CURRENT_BALANCE)

    CURSOR.execute('''
        INSERT INTO
            user_account(
                username,
                account_balance
                )
        VALUES(
            ?, ?  
            )
    ;''', FIRST_TIME_INFO)

    CONNECTION.commit()

class User:
    '''
    class to view the account
    '''
    def __init__(self, USER_INFO):
        self.USERNAME = USER_INFO[0]
        self.BALANCE = USER_INFO[1]
        self.TRANSACTIONS = [USER_INFO[2]]
        print(self.TRANSACTIONS)

    ### MODIFIERS ###
    def widthdrawMoney(self):
        '''
        spend money from your current balance
        :return: None
        '''
        AMOUNT_SPENT = checkInt(input("Money Spent: "))

        if AMOUNT_SPENT > self.BALANCE:
            PROCEED = input("You don't have enough money, would you like to go in debt? (Y/n) ")
        if PROCEED == "n" or PROCEED == "N":
            self.menu() # go back to menu

        LOCATION = input("Location: ")
        DATE = date.today()
        TYPE = "Withdrawal"
        TRANSACTION = (AMOUNT_SPENT, LOCATION, DATE.strftime("%Y/%m/%d"), TYPE)
        self.TRANSACTIONS.append(TRANSACTION)
        self.BALANCE = self.BALANCE - AMOUNT_SPENT

    def depositMoney(self):
        '''
        add money to your current balance
        :return: None
        '''
        AMOUNT = checkInt(input("Money Earned: "))
        LOCATION = input("Location: ")
        DATE = date.today()
        TYPE = "Deposit"
        TRANSACTION = [AMOUNT, LOCATION, DATE.strftime("%Y/%m/%d"), TYPE]
        self.TRANSACTIONS.append(TRANSACTION)
        self.BALANCE = self.BALANCE + AMOUNT

    def storeData(self):
        '''
        stores the data into the sql database
        :return: None
        '''
        TRANSACTIONS = str(self.TRANSACTIONS)
        NEW_DATA = (self.BALANCE, TRANSACTIONS)
        print(NEW_DATA)

        CURSOR.execute('''
            INSERT INTO
                user_account(
                    account_balance,
                    transactions
                    )
            VALUES(
                ?, ? 
                )
        ;''', NEW_DATA)

        CONNECTION.commit()

    ### ACCESSORS ###
    def viewBalance(self):
        '''
        displays the balance
        :return: None
        '''
        print(f"Balance: ${self.BALANCE}")

    def viewTransactions(self):
        '''
        check previously made transactions
        :return: None
        '''
        for TRANSACTION in self.TRANSACTIONS:
            print(TRANSACTION)

    def menu(self):
        '''
        pick option to perform a certain task
        :return: None
        '''
        OPTION = checkInt(input('''\nPick an option from the list below
1. Check Balance
2. See Previous Transactions
3. Make a Transaction
4. Exit
> '''))

        if OPTION == 1:
            self.viewBalance()
        elif OPTION == 2:
            self.viewTransactions()
        elif OPTION == 3:
            TRANSACTION_TYPE = checkInt(input('''Would you like to:
1. Deposit Money
2. Withdraw Money
> '''))
            if TRANSACTION_TYPE == 1:
                self.depositMoney()
            elif TRANSACTION_TYPE == 2:
                self.widthdrawMoney()
        else:
            self.storeData()
            exit()
        sleep(0.3)
        return self.menu()

if __name__ == "__main__":
    print("Welcome to Budgy!")

    if FIRST_RUN:
        createDatabase()
        getUserInfo()

    # get info from database
    INFO = CURSOR.execute('''
        SELECT * FROM user_account
    ;''').fetchone()

    print(INFO)

    USER = User(INFO)

    USER.menu()

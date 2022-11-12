'''
title: main class to view user account
author: Ayaan Merchant
date-created: 2022-01-07
'''

import sqlite3, pathlib, money, functions, checkingsAccount

### VARIABLES ###
DB_FILE = "user_account.db"
FIRST_RUN = True

if (pathlib.Path.cwd() / DB_FILE).exists():
    FIRST_RUN = False # don't create DB if already created

CONNECTION = sqlite3.connect(DB_FILE)
CURSOR = CONNECTION.cursor()

## create databases and do account set up
def createDatabases():
    '''
    create the databases for user account & transactions
    :return: None
    '''

    CURSOR.execute('''
        CREATE TABLE
            user_account(
                username TEXT NOT NULL PRIMARY KEY,
                balance_checking INT NOT NULL,
                balance_saving INT NOT NULL
            )
    ;''')

    CURSOR.execute('''
        CREATE TABLE
            user_transactions(
                transaction_amount INT NOT NULL,
                transaction_location TEXT NOT NULL,
                transaction_date TEXT NOT NULL,
                transaction_type TEXT NOT NULL
            )
    ;''')

def getUserInfo():
    '''
    when first run, get and store user info in DB
    :return: None
    '''
    print("Thank-you for choosing Budgy")
    print("Since this is your first time using Budgy, we will be setting up your account \n")

    NAME = input("Your Name: ")
    BALANCE_CHECKING = functions.checkInt(input("Your Checking Account's Balance (this can be updated later): "))
    BALANCE_SAVINGS = functions.checkInt(input("Your Saving Account's Balance (this can be updated later): "))
    print("Thank-you! Your account has been set up!")

    FIRST_TIME_INFO = [NAME, BALANCE_CHECKING, BALANCE_SAVINGS]

    CURSOR.execute('''
        INSERT INTO
            user_account(
                username,
                balance_checking,
                balance_saving
                )
        VALUES(
            ?, ?, ?
            )
    ;''', FIRST_TIME_INFO)

    CONNECTION.commit()

def saveTransaction(TRANSACTION):
    '''
    store the transaction in the database
    :param TRANSACTION: (list) of transaction info
    :return: None
    '''

    CURSOR.execute('''
            INSERT INTO
                user_transactions
            VALUES(
                ?, ?, ?, ?
            )
        ;''', TRANSACTION) # amount, location, date, type

    CONNECTION.commit()

def storeUserData(BALANCE, BALANCE_CHECKING, BALANCE_SAVINGS):
    '''
    store  data in database upon program exit
    :param BALANCE: (int) current account balance
    :return: None
    '''
    NEW_DATA = [BALANCE, BALANCE_CHECKING, BALANCE_SAVINGS]

    CURSOR.execute('''
        UPDATE
            user_account,
        SET
            ?, ?, ?
    ;''', NEW_DATA)

## Program Classes
class User:
    '''
    class to view the account

    :methods:
    - menu()
    - makeTransaction()
    - viewBalance()
    - viewTransactions

    :attributes:
    - USERNAME
    - BALANCE
    - TRANSACTIONS
    '''
    def __init__(self, USER_DATA, USER_TRANSACTIONS):
        self.USERNAME = USER_DATA[0]
        self.BALANCE_CHECKING = USER_DATA[1]
        self.BALANCE_SAVINGS = USER_DATA[2]
        self.TRANSACTIONS = USER_TRANSACTIONS

    ### MODIFIERS ###
    def makeTransaction(self):
        '''
        spend money from your current balance
        :return: None
        '''
        TRANSACTION = money.Transaction(self.BALANCE)

        TRANSACTION_TYPE = functions.checkInt(input('''Would you like to:
1. Deposit Money
2. Withdraw Money
> '''))

        if TRANSACTION_TYPE == 1:
            TRANSACTION.deposit()
        elif TRANSACTION_TYPE == 2:
            TRANSACTION.widthdrawl()

        # do the transaction
        self.BALANCE = TRANSACTION.getNewBal()
        saveTransaction(TRANSACTION.getTransaction())
        print(f'Transaction Completed; ${self.BALANCE} is your new balance')

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
        COUNT = 1
        for TRANSACTION in self.TRANSACTIONS:
            print(f"{COUNT}. {TRANSACTION}")
            COUNT += 1

    ### MENU TO NAVIGATE THE ENTIRE USER ACCOUNT ###
    def menu(self):
        '''
        pick option to perform a certain task, created in user class for efficiency
        :return: None
        '''
        OPTION = functions.checkInt(input('''\nPick an option from the list below
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
            self.makeTransaction()
        else:
            storeData(self.BALANCE)
            exit()
        return self.menu()

def selectAccount():
    '''
    selects either savings or checking account
    :return: (int) selected option
    '''
    ACCOUNT = functions.checkInt(input('''\nWhich account would you like to log into
    1. Checking Account
    2. Saving Account
    > '''))

    if ACCOUNT != 1 or ACCOUNT !=2:
        print("Select from the Options Listed.")
        return selectAccount()

if __name__ == "__main__":
    print("Welcome to Budgy!")

    if FIRST_RUN == True:
        createDatabases()
        getUserInfo()

    # get info from database
    USER_DATA = CURSOR.execute('''
        SELECT * FROM user_account
    ;''').fetchone()

    USER_TRANSACTIONS = CURSOR.execute('''
        SELECT * FROM user_transactions
    ;''').fetchall()

    # insert info and initiate class
    USER = User(USER_DATA, USER_TRANSACTIONS)

    USER.menu()



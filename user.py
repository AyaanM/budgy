'''
title: class to see account
author: Ayaan Merchant
date-created: 2022-01-07
'''

import money
from datetime import date
from time import sleep

### VARIABLES ###
FILE = ##SQL FILE##


def checkInt(NUM):
    try:
        NUM = float(NUM)
        return NUM
    except ValueError:
        NEW_NUM = input("Input must be a number: ")
        return checkInt(NEW_NUM)

class User:
    '''
    class to view the account
    '''
    def __init__(self):
        self.BALANCE = 0
        self.TRANSACTIONS = []

    ### MODIFIERS ###
    def widthdrawMoney(self):
        '''
        spend money from your current balance
        :return: None
        '''
        AMOUNT = checkInt(input("Money Spent: "))
        LOCATION = input("Location: ")
        DATE = date.today()
        TYPE = "Withdrawal"
        TRANSACTION = money.Transaction(AMOUNT, LOCATION, DATE, TYPE)
        self.TRANSACTIONS.append(TRANSACTION)
        self.BALANCE = self.BALANCE - AMOUNT

    def depositMoney(self):
        '''
        add money to your current balance
        :return: None
        '''
        AMOUNT = checkInt(input("Money Earned: "))
        LOCATION = input("Location: ")
        DATE = date.today()
        TYPE = "Deposit"
        TRANSACTION = money.Transaction(AMOUNT, LOCATION, DATE, TYPE)
        self.TRANSACTIONS.append(TRANSACTION)
        self.BALANCE = self.BALANCE + AMOUNT

    ### ACCESSORS ###
    def viewBalance(self):
        '''
        displays the balance
        :return: None
        '''
        print(f"Balance: {self.BALANCE}")

    def viewTransactions(self):
        '''
        check previously made transactions
        :return: None
        '''
        for i in range(len(self.TRANSACTIONS)):
            print(f'''# {i+1}
    {self.TRANSACTIONS[i].AMOUNT}
    {self.TRANSACTIONS[i].LOCATION}
    {self.TRANSACTIONS[i].DATE}
    {self.TRANSACTIONS[i].TYPE}''')

    def menu(self):
        '''
        pick option to perform a certain task
        :return: None
        '''
        print("")
        OPTION = checkInt(input('''Pick an option from the list below
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
            exit()
        sleep(0.3)
        return self.menu()

if __name__ == "__main__":
    USER = User()
    print("Welcome to Budgy!")

    ### open sql file for user ###



    USER.menu()

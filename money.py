'''
title: class to manage money
author: Ayaan Merchant
date-created: 2022-01-07
'''

import functions
from datetime import date

class Transaction:
    '''
    store the transaction
    '''

    def __init__(self, CURRENT_BALANCE):
        self.TRANSACTION = []
        self.BALANCE = CURRENT_BALANCE

    ### --- MODIFIERS --- ###
    def widthdrawl(self):
        '''
        spend money from your current balance
        :return: None
        '''
        AMOUNT = functions.checkInt(input("Money Spent: "))

        '''if AMOUNT_SPENT > self.BALANCE:
            PROCEED = input("You don't have enough money, would you like to go in debt? (Y/n) ")
            if PROCEED == "n" or PROCEED == "N":
                return user.User.menu()  # go back to menu'''

        LOCATION = input("Location: ")
        DATE = date.today().strftime("%Y/%m/%d")
        TYPE = "Withdrawal"
        self.TRANSACTION = [AMOUNT, LOCATION, DATE, TYPE]
        self.BALANCE = self.BALANCE - self.AMOUNT

    def deposit(self):
        '''
        deposit money to current balance
        :return:
        '''
        AMOUNT = functions.checkInt(input("Money Earned: "))
        LOCATION = input("Location: ")
        DATE = date.today()
        TYPE = "Deposit"

        self.TRANSACTION = [AMOUNT, LOCATION, DATE, TYPE]
        self.BALANCE = self.BALANCE + self.AMOUNT

    ### --- ACCESSORS --- ###
    def getTransaction(self):
        '''
        return the transaction
        :return: list
        '''
        return self.TRANSACTION

    def getNewBal(self):
        '''
        returns the new balance after the transaction
        :return: int
        '''
        return self.BALANCE
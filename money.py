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
        AMOUNT_SPENT = functions.checkInt(input("Money Spent: "))

        '''if AMOUNT_SPENT > self.BALANCE:
            PROCEED = input("You don't have enough money, would you like to go in debt? (Y/n) ")
            if PROCEED == "n" or PROCEED == "N":
                return user.User.menu()  # go back to menu'''

        LOCATION = input("Location: ")
        DATE = date.today()
        TYPE = "Withdrawal"
        self.TRANSACTION = [AMOUNT_SPENT, LOCATION, DATE.strftime("%Y/%m/%d"), TYPE]
        self.BALANCE = self.BALANCE - AMOUNT_SPENT

    def deposit(self):
        '''
        deposit money to current balance
        :return:
        '''
        AMOUNT = functions.checkInt(input("Money Earned: "))
        LOCATION = input("Location: ")
        DATE = date.today()
        TYPE = "Deposit"

        self.TRANSACTION = [AMOUNT, LOCATION, DATE.strftime("%Y/%m/%d"), TYPE]
        self.BALANCE = self.BALANCE + AMOUNT

    ### --- ACCESSORS --- ###
    def getTransaction(self):
        '''
        return the transaction
        :return: array
        '''
        return self.TRANSACTION

    def getNewBal(self):
        '''
        returns the new balance after the transaction
        :return: int
        '''
        return self.BALANCE
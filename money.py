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

    def __init__(self, AMOUNT, LOCATION, CURRENT_BALANCE, ACCOUNT_TYPE):
        self.TRANSACTION = []
        self.AMOUNT = AMOUNT
        self.LOCATION = LOCATION
        self.DATE = date.today()
        self.BALANCE = CURRENT_BALANCE
        self.ACCOUNT = ACCOUNT_TYPE
        

    ### --- MODIFIERS --- ###
    def deposit(self):
        '''
        deposit money to current balance
        :return:
        '''
        self.TRANSACTION = [self.AMOUNT, self.LOCATION, self.DATE, "Deposit", self.ACCOUNT]
        self.BALANCE = self.BALANCE + self.AMOUNT

    def widthdrawl(self):
        '''
        spend money from your current balance
        :return: None
        '''
        self.TRANSACTION = [self.AMOUNT, self.LOCATION, self.DATE, "Withdrawal", self.ACCOUNT]
        self.BALANCE = self.BALANCE - self.AMOUNT

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
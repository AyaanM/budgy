'''
title: class to manage money
author: Ayaan Merchant
date-created: 2022-01-07
'''

class ManageMoney:
    '''
    manage money by either adding or deducting money from current balance
    '''

    def __init__(self, AMOUNT, CURRENT_BALANCE):
        self.AMOUNT = AMOUNT
        self.BALANCE = CURRENT_BALANCE

    def addMoney(self):
        self.BALANCE = self.BALANCE + self.AMOUNT

    def deductMoney(self):
        self.BALANCE = self.BALANCE - self.AMOUNT

class Transaction():
    '''
    store the transaction
    '''
    def __init__(self, AMOUNT, LOCATION, DATE, TYPE):
        self.AMOUNT = AMOUNT
        self.LOCATION = LOCATION
        self.DATE = DATE
        self.TYPE = TYPE


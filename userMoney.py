'''
title: class to manage money
author: Ayaan Merchant
date-created: 2022-01-07
'''

import functions
from datetime import date

class Transaction: # store the transaction
    def __init__(self, AMOUNT, LOCATION, CURRENT_BALANCE, ACCOUNT_TYPE):
        self.TRANSACTION = []
        self.AMOUNT = AMOUNT
        self.LOCATION = LOCATION
        self.BALANCE = CURRENT_BALANCE
        self.ACCOUNT = ACCOUNT_TYPE

    def create(self):
        TRANSACTION_TYPES = ["Deposit", "Widthdrawl"]
        print("Choose a transaction type")
        for i in range(len(TRANSACTION_TYPES)):
            print(f"{i+1}. {TRANSACTION_TYPES[i]}")
        TYPE = functions.checkInt(input("> "))-1

        self.TRANSACTION = [self.AMOUNT, self.LOCATION, date.today(), TRANSACTION_TYPES[TYPE], self.ACCOUNT]
        
        if TYPE == 0:
            self.BALANCE = self.BALANCE + self.AMOUNT
        else:
            self.BALANCE = self.BALANCE - self.AMOUNT

        return self.TRANSACTION, self.BALANCE
        
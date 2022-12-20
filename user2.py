'''
main class to view the user account (V2 as V1 was unreadable)
author: Ayaan Merchant
date-created: 2022-11-16
'''

from pathlib import Path
from databases import user_database
import functions

if not Path("user_account.db").exists():
    FIRST_RUN = True
else: FIRST_RUN = False

class User: # class to run the user program
    
    def __init__(self, USER_DATA, USER_TRANSACTIONS):
        self.USERNAME = USER_DATA[0]
        self.ACCOUNTS_BALANCE = [USER_DATA[2], USER_DATA[3]] # checkings, savings
        self.TRANSACTIONS = USER_TRANSACTIONS

    def viewBalance(self): #displays balance
        print(f"Checkings Account: ${self.ACCOUNTS_BALANCE[0]}")
        print(f"Savings Account: ${self.ACCOUNTS_BALANCE[1]}")

    def viewTransactions(self): #displays transactions
        print(True)
        for TRANSACTION in self.TRANSACTIONS:
            print(f"{i+1}. {TRANSACTION}")

    def menu(self): # pick option to perform task

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
                #USER_ACCOUNT.storeData(self.USERNAME, self.ACCOUNTS_BALANCE)
                exit()
            return self.menu()

if __name__ == "__main__":
    USER_ACCOUNT = user_database() # initiate the DB
    
    if FIRST_RUN == True: 
        print("Thank-you for choosing Budgy.")
        print("Since this is your first time using Budgy, we will be setting up your account.\n")
        USER_ACCOUNT.createAccount()
        print("\nThank-you! Your account has been set up!")

    USER_DATA, USER_TRANSACTIONS = USER_ACCOUNT.get_info()

    USER = User(USER_DATA, USER_TRANSACTIONS)

    USER.menu()

    
    








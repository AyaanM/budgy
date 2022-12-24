'''
main class to view the user account (V2 as V1 was unreadable)
author: Ayaan Merchant
date-created: 2022-11-16
'''
## THE WORD USER SIGNIFIES THE USER OF THE ACCOUNT, AND THE WORD ACCOUNT SIGNIFIES THE ACCOUNT AS A WHOLE (THE USER AND THEIR ACCOUNT PROPERTIES)

from pathlib import Path
from databases import user_database
import functions, userMoney

if not Path("user_account.db").exists():
    FIRST_RUN = True
else: FIRST_RUN = False

class user_account: # class to run the user program
    
    def __init__(self, ACCOUNT_DATA, ACCOUNT_TRANSACTIONS):
        self.USER_INFO = [ACCOUNT_DATA[0], ACCOUNT_DATA[1]] # username, password
        self.ACCOUNTS_BALANCE = [ACCOUNT_DATA[2], ACCOUNT_DATA[3]] # checkings, savings
        self.TRANSACTIONS = ACCOUNT_TRANSACTIONS # transactions that already took place (from db)
        self.NEW_TRANSACTIONS = [] # transactions that will be made in this run of program
        self.ACCOUNTS = ["Checkings", "Savings"]

    def viewBalance(self): # displays balance
        print(f"{self.ACCOUNTS[0]} Account: ${self.ACCOUNTS_BALANCE[0]}")
        print(f"{self.ACCOUNTS[1]} Account: ${self.ACCOUNTS_BALANCE[1]}")

    def viewTransactions(self): # displays transactions
        TRANSACTIONS = self.TRANSACTIONS + self.NEW_TRANSACTIONS
        for i in range(len(TRANSACTIONS)):
            print(f"{i+1}. {TRANSACTIONS[i]}")

    def makeTransaction(self):
        print("These are the accounts you currently have.")
        for i in range(len(self.ACCOUNTS)):
            print(f"{i+1}. {self.ACCOUNTS[i]}")
        ACCOUNT = functions.checkInt(input("Make transaction from (select account) > "))-1
        AMOUNT = functions.checkInt(input("Money: "))
        LOCATION = input("Location: ")
        TRANSACTION = userMoney.Transaction(AMOUNT, LOCATION, self.ACCOUNTS_BALANCE[ACCOUNT], self.ACCOUNTS[ACCOUNT])
        TRANSACTION, self.ACCOUNTS_BALANCE[ACCOUNT] = TRANSACTION.create()
        self.NEW_TRANSACTIONS.append(TRANSACTION)
        print(f"Transaction Complete, ${self.ACCOUNTS_BALANCE[ACCOUNT]} is your new {self.ACCOUNTS[ACCOUNT]} balance.")

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
                USER_DATABASE.storeData(self.USER_INFO, self.ACCOUNTS_BALANCE, self.NEW_TRANSACTIONS)
                exit()
            return self.menu()

if __name__ == "__main__":
    USER_DATABASE = user_database() # initiate the DB
    
    if FIRST_RUN == True: 
        print("Thank-you for choosing Budgy.")
        print("Since this is your first time using Budgy, we will be setting up your account.\n")
        USER_DATABASE.createAccount()
        print("\nThank-you! Your account has been set up!")

    ACCOUNT_DATA, ACCOUNT_TRANSACTIONS = USER_DATABASE.get_info()

    USER_ACCOUNT = user_account(ACCOUNT_DATA, ACCOUNT_TRANSACTIONS)

    USER_ACCOUNT.menu()

    
    








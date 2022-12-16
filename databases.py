'''
file where all the processes considering user databases will take place (done to unclutter main user file)
author: Ayaan Merchant
date-created: 2022-11-16
'''

def createAccount(): # database to store user account

    CURSOR.execute('''
        CREATE TABLE
            user_account(
                username TEXT NOT NULL PRIMARY KEY,
                password TEXT NOT NULL,
                balance_checking INT NOT NULL,
                balance_saving INT NOT NULL
            )
    ;''')

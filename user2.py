'''
main class to view the user account (V2 as V1 was unreadable)
author: Ayaan Merchant
date-created: 2022-11-16
'''

from pathlib import Path
import sqlite3, createAccount

# create DB file
USER_ACCOUNT = "user_account.db"
USER_FILE = Path("user_account.db")

if not USER_FILE.exists():
    databases.createAccount()


# connect and cursor the DB file
CONNECTION = sqlite3.connect("user_account.db")
CURSOR = CONNECTION.cursor()


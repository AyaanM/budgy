'''
title: funtions to be used with program
author: Ayaan Merchant
date: 2022-03-26
'''
def checkInt(NUM):
    try:
        NUM = int(NUM)
        return NUM
    except ValueError:
        NEW_NUM = input("Input must be a number: ")
        return checkInt(NEW_NUM)

def checkSamePass(PASS1, PASS2):
    for i in range(2):
        if PASS1 != PASS2:
            print("Passwords Don't Match! Please Try Again")
            PASS1 = input("Password: ")
            PASS2 = input("Confirm Password: ")
        if PASS1 == PASS2:
            return True
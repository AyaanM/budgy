'''
title: funtions to be used with program
author: Ayaan Merchant
date: 2022-03-26
'''
def checkInt(NUM):
    try:
        NUM = float(NUM)
        return NUM
    except ValueError:
        NEW_NUM = input("Input must be a number: ")
        return checkInt(NEW_NUM)
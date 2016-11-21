'''
Created on Oct 20, 2016
Intro to Python Programming - CSUF
Lab 4: Standard Modules, Packages, and Classes
BankCustomer Driver
lab4.py
@author: Javier Chavarela
'''


from W4.BankCustomer import BankCustomer

bankCustomer = BankCustomer("Tom Thumb", 3000000.00)
bankCustomer.withdraw(100.00)
bankCustomer.deposit(10000.00)
bankCustomer.withdraw(10000000.00)

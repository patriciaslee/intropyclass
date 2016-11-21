'''
Created on Oct 20, 2016
Intro to Python Programming - CSUF
Lab 4: Standard Modules, Packages, and Classes
Class BankCustomer
BankCustomer.py
@author: Javier Chavarela
'''


class BankCustomer:

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = float(balance)
        print("Hi, %s!" % name)

    def withdraw(self, amountWithdrawal):
        if amountWithdrawal > self.balance:
            print("*******************************************************\n"
                  "Amount greater than available balance!!!\n"
                  "Balance: $%s \nDesired withdrawal amount: $%s "
                  % ("{:,.2f}".format(self.balance),
                     "{:,.2f}".format(amountWithdrawal)))

        else:
            self.balance -= amountWithdrawal
            print("After a withdrawal of $%s, "
                  "here is your current balance: $%s"
                  % ("{:,.2f}".format(amountWithdrawal),
                     "{:,.2f}".format(self.balance)))

    def deposit(self, amountDeposit):
        self.balance += amountDeposit
        print("After a deposit of $%s, here is your current balance: $%s"
              % ("{:,.2f}".format(amountDeposit),
                 "{:,.2f}".format(self.balance)))

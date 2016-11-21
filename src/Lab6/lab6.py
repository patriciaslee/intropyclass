#Python Lab4.py - Module Bank Customer Driver
#get balance, deposite and withdrawal amount

from BankCustomer import BankCustomer

user = BankCustomer("Nimesh", 3000000)

user.getCustomerName()
user.getBalance()

user.setDeposit(100)
user.getDeposit()

user.setWithdrawal(200)
user.getWithdrawal()

user.setDeposit(10000)
user.getDeposit()

user.setWithdrawal(10000000)
user.getWithdrawal()

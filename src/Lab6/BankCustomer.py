#Python BankCustomer.py - Module   (for lab4.py)
#get balance, deposite and withdrawal amount

#Open Issue: How we could monitor Customer access entry info
#placed it into a log file for further review on Customer activity.
# - How can we modify this code?

import locale

#String defind var
str1  = 'Desired Withdrawal Amount: '
str2A = 'After Withdrawal of '
str2B = ' here is your current Balance: '
str3  = 'Desired Deposit Amount: '
str4A = 'After Deposite of '
str4B = ' here is your Balance: '
str4C = 'Current Balance is '
str5  = '-->Withdrawal Amount is greater than available Balance!!!'
str6  = '*****************************************'
str7  = 'After trying a Withdrawal of '

#intialize(just for record)
balance  = 0.00
userName = 'Jude'

#Define two classes: BankCustomer and Balance
#############################################
class BankCustomer:
    def __init__(self, userName, balance):
        self.name    = userName
        self.balance = balance

    #Display customer Name
    ######################
    def setCustomerName(self, userName):
        self.name = userName
    
    def getCustomerName(self ):
        print("Welcome to the My Bank, %s" % self.name )
        return(self.name )

    #getBalance
    ###########
    def setBalance(self, balance ):
        self.balance = balance
                    
    #getBalance
    ###########
    def getBalance(self):
        strBal = '${:,.2f}'.format(self.balance)
        print("%s %s\n" % (str4C, strBal) )                    
        return(self.balance )

    #setDeposit Money
    #################
    def setDeposit(self, deposit):
        #deposit = input(str3)
        self.deposit = float(deposit)

        #set the new balance
        self.balance += self.deposit      
      
    #setDeposit Money
    #################
    def getDeposit(self):
        strBal = '${:,.2f}'.format(self.balance)
        strDep = '${:,.2f}'.format(self.deposit)
        print(str4A + strDep + str4B + strBal)
        return(self.deposit, self.balance)

    #setWithdraw Money
    ###############
    def setWithdrawal(self, withdraw):
        #withdraw = input(str1)
        self.withdraw = float(withdraw)

    #getWithdraw Money
    ###############
    def getWithdrawal(self):
        strBal  = '${:,.2f}'.format(self.balance)
        strWith = '${:,.2f}'.format(self.withdraw)

        if (self.withdraw <= self.balance ):
            self.balance -= self.withdraw

            strBal  = '${:,.2f}'.format(self.balance)
            strWith = '${:,.2f}'.format(self.withdraw)
            print(str2A + strWith + str2B + strBal) 
        else:
            print("Requested to Withdraw %s " % strWith )
            print('\n%s \n Warning: Withdrawal could not be made \n %s\n' % (str6, str5) )
            print(str4C + strBal + '\n' + str1 + strWith) 
            print(str7 + strWith + str4B + strBal + '\n\n') 

        return( self.withdraw, self.balance )





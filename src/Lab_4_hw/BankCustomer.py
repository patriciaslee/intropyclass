class BankCustomer:
    def __init__(self, cust_name, opening_balance):
        self.name = cust_name
        self.balance = float(opening_balance)

        print("Hi, " + self.name + "!")

    def withdraw(self, amount):
        if (amount > self.balance):
            message = print ("Amount greater than available balance!!!\n" \
                             "Balance: " + str (amount) + "\n" \
                             "Desired withdrawal amount: " + str(amount) + "\n" \
                             "After trying a withdrawal of $" + str(amount) + ", here is your balance: " + str(self.balance))
            return message
        else:
            self.balance -=amount
            message = print("After a withdrawal of $" + str(amount) + ".00, here is your current balance: " + str(self.balance))
            return message
    
    def deposit(self, amount):
        self.balance += amount
        asterisk = "*" * 45
        message = print("After a deposit of $" + str(amount) + ", here is your balance: " + str(self.balance) + "\n" \
                        + asterisk)
        return message


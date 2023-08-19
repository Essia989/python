class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate= 0.5, balance= 0): 
        self.balance = balance
        self.int_rate = int_rate
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount < self.balance: 
            self.balance -= amount
        else: 
            self.balance -= 5
            print ("Insufficient funds: Charging a $5 fee")
        return self
    def display_account_info(self):
        print ("Balance: $" + str(self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
        return self
    
    def account_details(self):
        print("---------------------------- Account Details ------------------------------------\n")
        print(f"Account Balance : $ {self.balance} \nInterest Rate : % {self.int_rate}")
        return self
    

Account_1 = BankAccount(0.8,2000)
Account_2 = BankAccount(0.5,750)

print("----------------------------Account 1------------------------------------\n")
Account_1.deposit(250).deposit(300).deposit(100).withdraw(400).display_account_info().account_details()

print("----------------------------Account 2------------------------------------\n")
Account_2.deposit(100).deposit(250).withdraw(400).withdraw(400).withdraw(400).withdraw(400).yield_interest().display_account_info().account_details()

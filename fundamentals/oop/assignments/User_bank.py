from BankAccount import BankAccount

class User:
    def __init__(self,firstname,lastname,email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.Nbr_accounts = 1
        self.accounts = [{ "acc_Nbr" : self.Nbr_accounts, "account": BankAccount()}]

    def make_deposit(self, amount, Nbr_acc = 0):
        self.accounts[Nbr_acc]["account"].deposit(amount)
        return self

    def make_withdrawal(self, amount, Nbr_acc = 0):
        self.accounts[Nbr_acc]["account"].withdraw(amount)
        return self

    def add_account(self, amount):
        self.Nbr_accounts += 1
        self.accounts.append({"acc_Nbr" : self.Nbr_accounts, "account": BankAccount(amount)})
        return self
    
    def display_user_balance(self,Nbr_acc = 0):
        print(f"User : {self.firstname}, Balance : {self.accounts[Nbr_acc]['account'].balance}")
        return self

    def transfer_money(self, other_user, amount, Nbr_acc = 0):
        if self.accounts[Nbr_acc]["account"].balance > amount:
            self.accounts[Nbr_acc]["account"].balance -= amount
            other_user.accounts[Nbr_acc]["account"].balance += amount
            print (self.display_user_balance(),other_user.display_user_balance())
            return self,other_user
        else:
            self.accounts[Nbr_acc]["account"].balance -= 5
            print ("Insufficient funds: Charging a $5 fee")
            return self

Essia = User("Essia","Mahmoudi","Essiamahmoudi@gmail.com")
Alex = User("Alex","Good","Alexx_good@gmail.com")
Sana = User("Sana","Belhaj","Sana1235@gmail.com")

print("------------------------------ Essia Transactions -----------------------------------")

Essia.display_user_balance().make_deposit(300).display_user_balance().make_withdrawal(300).display_user_balance().transfer_money(Alex,100)
Essia.display_user_balance()
#Alex.deposit(2000).deposit(150).make_withdrawal(150).make_withdrawal(400).display_user_balance()

print("----------------------------- Alex Transactions ------------------------------------")

Alex.transfer_money(Essia,300).display_user_balance()
Alex.display_user_balance().make_deposit(700).display_user_balance().make_withdrawal(200).display_user_balance().transfer_money(Sana,200)

print("------------------------------ Sana Transactions -----------------------------------")
Sana.display_user_balance().make_deposit(250).display_user_balance().make_withdrawal(80).display_user_balance().transfer_money(Essia,300)
Essia.display_user_balance()
Sana.display_user_balance()
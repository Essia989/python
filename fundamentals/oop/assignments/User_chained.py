class User:
    def __init__(self,firstname,lastname,email,balance):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User : {self.firstname}, Balance : {self.balance}")

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self,other_user

Essia = User("Essia","Mahmoudi","Essiamahmoudi@gmail.com",1000)
Alex = User("Alex","Good","Alexx_good@gmail.com",2500)
Sana = User("Sana","Belhaj","Sana1235@gmail.com",4500)

Essia.deposit(2500).deposit(460).deposit(1850).make_withdrawal(385).display_user_balance()

print("-----------------------------------------------------------------")

Alex.deposit(2000).deposit(150).make_withdrawal(150).make_withdrawal(400).display_user_balance()

print("-----------------------------------------------------------------")

Sana.deposit(3000).make_withdrawal(250).make_withdrawal(1010).make_withdrawal(330).display_user_balance()

print("-----------------------------------------------------------------")
Essia.transfer_money(Sana,200).display_user_balance()
Sana.display_user_balance()
#Create a program for a Bank System using Hierarchical Inheritance


class BankAccount:
    def __init__(self,account_holder):
        self.balance=0
        self.account_holder=account_holder
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            self.display_balance()
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("The account balance is:",self.balance)

class SavingsAccount(BankAccount):
    def __init__(self,account_holder,intrest_rate):
        self.intrest_rate=intrest_rate
        super().__init__(account_holder)
    def add_intrest(self):
        intrest=self.balance*self.intrest_rate/100
        self.balance=self.balance+intrest
        super().display_balance()

class CurrentAccount(BankAccount):
    def __init__(self,account_holder,overdraft_limit):
        self.overdraft_limit=overdraft_limit
        super().__init__(account_holder)
    def withdraw_with_overdraft(self,amount):
        if self.balance+self.overdraft_limit>=amount:
            self.balance-=amount
            super.display_balance()
        else:
            print("overdraft limit exceeded")
save=SavingsAccount("Roja",2)
current=CurrentAccount("Anil",500)
save.deposit(100)
save.withdraw(20)
save.add_intrest()
            




          

#Create a program for a Bank System using Hierarchical Inheritance


class BankAccount:
    def __init__(self,account_holder,balance,):
        self.balance=balance
        self.account_holder=account_holder
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def display_balance(self):
        print("Account holder:",self.account_holder)
        print("The account balance is:",self.balance)

class SavingsAccount(BankAccount):
    def __init__(self,account_holder,balance,intrest_rate):
        self.intrest_rate=intrest_rate
        super().__init__(account_holder,balance)
    def add_intrest(self):
        intrest=self.balance*self.intrest_rate/100
        self.balance=self.balance+intrest

class CurrentAccount(BankAccount):
    def __init__(self,account_holder, balance,overdraft_limit):
        self.overdraft_limit=overdraft_limit
        super().__init__(account_holder,balance)
    def withdraw_with_overdraft(self,amount):
        if self.balance+self.overdraft_limit>=amount:
            self.balance+=amount
        else:
            print("overdraft limit exceeded")
save=SavingsAccount("Roja",10000,2)
current=CurrentAccount("Anil",50000,500)
save.display_balance()
            




          

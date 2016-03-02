#Charles Lynch
#Bank accountant

class Account:
    def __init__(self, id, balance, annualInterest):
        self.id = id
        self.balance = balance
        self.annaulInterest = annualInterest

    def getMonthlyRate(self):
        what = self.annaulInterest / 100  
        return what / 12
         
    def getMonthly(self):
        return self.balance * self.getMonthlyRate
        
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit (self, amount):
        self.balance += amount
        return self.balance

    def print (self):
        print (self.id)
        print (self.balance)
        print (self.getMonthlyRate())

card= Account(1122, 20000, 4.5)

card.withdraw(2500)
card.deposit(3000)
card.print()
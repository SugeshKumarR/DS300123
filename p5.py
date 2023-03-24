class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance =self.balance + amount

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.interestRate * self.balance/100)


demo1 = SavingsAccount("Mark", 2000, 5)
user1 = SavingsAccount("emo",500,5)
user1.deposit(200)
print(user1.getBalance())
print(user1.interestAmount())
user1.withdrawal(120)
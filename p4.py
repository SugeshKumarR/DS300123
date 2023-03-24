class Account:
    def __init__(self, title = None, balance = None ):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance = None,interestRate= None):
        super().__init__(title,balance)
        self.interestRate = interestRate
        print(f"Account({title}, {balance}, {interestRate})")

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate


account_obj = Account("Emon",5000)

savings_obj =SavingsAccount(account_obj)
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def depositAmount(self, amount):
        if amount > 0:
            self.balance += amount

    def withdrawalAmount(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, title, balance, interest_rate):
        super().__init__(title, balance)
        self.interest_rate = interest_rate

    def interestAmount(self):
        return ((self.interest_rate/100) * self.balance)/100

savings_account = SavingsAccount('Aashish', 5000, 5) 

print(f"Account Title: {savings_account.title}")
print(f"Initial Balance: ${savings_account.getBalance()}")

savings_account.depositAmount(500.0)
print(f"Balance after deposit: ${savings_account.getBalance()}")

savings_account.withdrawalAmount(200.0)
print(f"Balance after withdrawal: ${savings_account.getBalance()}")

interest = savings_account.interestAmount()
print(f"Interest Amount: ${interest:.2f}")
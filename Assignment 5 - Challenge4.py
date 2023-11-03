class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interest_rate):
        super().__init__(title, balance)
        self.interest_rate = interest_rate

savings_account = SavingsAccount("Aashish", 5000, 5)
print(f"Account Title: {savings_account.title}")
print(f"Account Balance: ${savings_account.balance}")
print(f"Interest Rate: {savings_account.interest_rate}%")
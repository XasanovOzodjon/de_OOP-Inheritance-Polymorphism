class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.02):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def get_interest(self):
        return self.balance * self.interest_rate

    def withdraw(self, amount):
        # SavingsAccount: faqat balansdan kam bo'lsa, yechib olish mumkin
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

class CheckingAccount(BankAccount):
    def __init__(self, balance=0, overdraft_limit=100):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # CheckingAccount: overdraft limitdan foydalanish mumkin
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        return False

def main():
    sa = SavingsAccount(balance=1000)
    print(f"Savings Account Balance: {sa.get_balance()}")
    print(f"Interest Earned: {sa.get_interest()}")

    ca = CheckingAccount(balance=500, overdraft_limit=200)
    print(f"balanse: {ca.get_balance()}")
    
    if ca.withdraw(600):
        print("Withdrawal successful.")
    else:
        print("Withdrawal error.")

if __name__ == "__main__":
    main()
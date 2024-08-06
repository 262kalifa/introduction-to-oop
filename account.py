class Account:
    def __init__(self, account_holder_name, account_number, balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return f"Account Balance: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}"
        else:
            return "Invalid deposit amount. Please enter a positive number."

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive number."
        elif amount > self.balance:
            return f"Insufficient funds. Your current balance is ${self.balance:.2f}."
        else:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}"

# CurrentAccount and SavingsAccount classes can inherit from Account
class CurrentAccount(Account):
    def __init__(self, account_holder_name, account_number, balance=0):
        super().__init__(account_holder_name, account_number, balance)

class SavingsAccount(Account):
    def __init__(self, account_holder_name, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_holder_name, account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of ${interest:.2f} applied. New Balance: ${self.balance:.2f}"

# Example usage:
current_account = CurrentAccount("John Doe", "12345678", 1000)
print(current_account.check_balance())   # Output: Account Balance: $1000.00
print(current_account.deposit(200))      # Output: Deposited $200.00. New Balance: $1200.00
print(current_account.withdraw(500))     # Output: Withdrew $500.00. New Balance: $700.00

savings_account = SavingsAccount("Jane Doe", "87654321", 1000, 0.03)
print(savings_account.check_balance())   # Output: Account Balance: $1000.00
print(savings_account.deposit(500))      # Output: Deposited $500.00. New Balance: $1500.00
print(savings_account.apply_interest())  # Output: Interest of $45.00 applied. New Balance: $1545.00

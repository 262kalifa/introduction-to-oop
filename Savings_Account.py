class SavingsAccount:
    def __init__(self, account_holder_name, account_number, balance=0, interest_rate=0.02):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate

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

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of ${interest:.2f} applied. New Balance: ${self.balance:.2f}"

# Example usage:
account = SavingsAccount("Jane Doe", "87654321", 1000, 0.03)
print(account.check_balance())    # Output: Account Balance: $1000.00
print(account.deposit(500))       # Output: Deposited $500.00. New Balance: $1500.00
print(account.apply_interest())   # Output: Interest of $45.00 applied. New Balance: $1545.00
print(account.withdraw(200))      # Output: Withdrew $200.00. New Balance: $1345.00

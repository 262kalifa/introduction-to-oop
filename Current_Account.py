class CurrentAccount:
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

# Example usage:
account = CurrentAccount("John Doe", "12345678", 1000)
print(account.check_balance())   # Output: Account Balance: $1000.00
print(account.deposit(200))      # Output: Deposited $200.00. New Balance: $1200.00
print(account.withdraw(500))     # Output: Withdrew $500.00. New Balance: $700.00
print(account.withdraw(800))     # Output: Insufficient funds. Your current balance is $700.00.

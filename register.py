import random

from account import Account, CurrentAccount, SavingsAccount

class Register:
    def __init__(self):
        self.accounts = {}

    def generate_account_number(self):
        return str(random.randint(10000000, 99999999))

    def create_account(self, account_type, account_holder_name, initial_deposit=0, interest_rate=0.02):
        account_number = self.generate_account_number()
        
        if account_type == "current":
            new_account = CurrentAccount(account_holder_name, account_number, initial_deposit)
        elif account_type == "savings":
            new_account = SavingsAccount(account_holder_name, account_number, initial_deposit, interest_rate)
        else:
            return "Invalid account type."

        self.accounts[account_number] = new_account
        return f"Account created successfully! Account Number: {account_number}"

    def get_account(self, account_number):
        return self.accounts.get(account_number, "Account not found.")

# Example usage:
register = Register()

# Create a Current Account
print(register.create_account("current", "John Doe", 1000))
# Output: Account created successfully! Account Number: 12345678

# Create a Savings Account
print(register.create_account("savings", "Jane Doe", 500, 0.03))
# Output: Account created successfully! Account Number: 87654321

# Fetch account information
account = register.get_account("12345678")
if isinstance(account, Account):
    print(account.check_balance())  # Output: Account Balance: $1000.00
else:
    print(account)  # Output: Account not found.

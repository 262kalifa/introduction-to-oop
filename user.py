from register import Register

class User:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.accounts = []

    def add_account(self, register, account_type, initial_deposit=0, interest_rate=0.02):
        account_number = register.create_account(account_type, self.name, initial_deposit, interest_rate)
        if "Account created successfully!" in account_number:
            account_number = account_number.split(": ")[-1]
            self.accounts.append(account_number)
            return f"Account {account_number} linked to user {self.name}."
        return account_number

    def get_accounts(self, register):
        if not self.accounts:
            return "No accounts linked to this user."
        
        account_details = []
        for account_number in self.accounts:
            account = register.get_account(account_number)
            if isinstance(account, str):
                account_details.append(f"Account {account_number}: {account}")
            else:
                account_details.append(f"Account {account_number}: {account.check_balance()}")
        
        return "\n".join(account_details)

    def update_contact_info(self, email=None, phone_number=None):
        if email:
            self.email = email
        if phone_number:
            self.phone_number = phone_number
        return "User contact information updated."

# Example usage:
register = Register()

# Create a user
user = User("John Doe", "johndoe@example.com", "555-1234")

# User creates and links a Current Account
print(user.add_account(register, "current", 1000))
# Output: Account 12345678 linked to user John Doe.

# User creates and links a Savings Account
print(user.add_account(register, "savings", 500, 0.03))
# Output: Account 87654321 linked to user John Doe.

# Get all linked accounts for the user
print(user.get_accounts(register))
# Output: 
# Account 12345678: Account Balance: $1000.00
# Account 87654321: Account Balance: $500.00

# Update user contact information
print(user.update_contact_info(email="newemail@example.com"))
# Output: User contact information updated.

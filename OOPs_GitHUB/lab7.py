class ATM:
    def __init__(self, account_holder, account_number, initial_balance, pin):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance
        self.pin = pin

    # Method to check balance
    def check_balance(self):
        print(f"Current Balance: ${self.balance}")

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
            self.check_balance()
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    # Method to change PIN
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN. Please try again.")

# Example usage
account = ATM("John Doe", "123456789", 1000, "1234")

# Checking balance
account.check_balance()

# Depositing money
account.deposit(500)

# Changing PIN
account.change_pin("1234", "5678")
account.change_pin("0000", "1111")  # This should fail due to incorrect old PIN

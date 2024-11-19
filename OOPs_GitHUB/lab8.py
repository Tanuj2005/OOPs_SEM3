class Account:
    def __init__(self, account_no, account_holder_name, balance):
        self.account_no = account_no
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.transaction_history = TransactionHistory()

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.add_transaction("Deposit", amount)
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.add_transaction("Withdrawal", amount)
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")


class SavingsAccount(Account):
    def __init__(self, account_no, account_holder_name, balance, withdrawal_limit):
        super().__init__(account_no, account_holder_name, balance)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Cannot withdraw {amount}. Limit: {self.withdrawal_limit}")
        else:
            super().withdraw(amount)


class CurrentAccount(Account):
    def __init__(self, account_no, account_holder_name, balance, overdraft_limit):
        super().__init__(account_no, account_holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            super().withdraw(amount)


class CheckingAccount(Account):
    def __init__(self, account_no, account_holder_name, balance, transaction_fee):
        super().__init__(account_no, account_holder_name, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        if self.balance >= total_amount:
            self.balance -= total_amount
            self.transaction_history.add_transaction("Withdrawal", amount)
            print(f"Withdrew {amount} with fee {self.transaction_fee}. New balance: {self.balance}")
        else:
            print("Insufficient funds for withdrawal including fees.")


class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction_type, amount):
        self.transactions.append({"type": transaction_type, "amount": amount})

    def show_history(self):
        if not self.transactions:
            print("No transactions found.")
        else:
            for i, transaction in enumerate(self.transactions, 1):
                print(f"{i}. {transaction['type']}: {transaction['amount']}")


# Example Usage
savings = SavingsAccount("SA123", "Alice", 5000, 2000)
savings.deposit(1000)
savings.withdraw(2500)
savings.withdraw(3000)
savings.transaction_history.show_history()

current = CurrentAccount("CA123", "Bob", 1000, 500)
current.withdraw(1200)
current.withdraw(2000)
current.transaction_history.show_history()

checking = CheckingAccount("CHK123", "Charlie", 2000, 50)
checking.withdraw(1900)
checking.withdraw(2100)
checking.transaction_history.show_history()

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        print(f"Current balance is {self.balance}.")

my_account = BankAccount("John Doe", 1000)
my_account.get_balance() # Output: Current balance is 1000.
my_account.deposit(500) # Output: Deposited 500. New balance is 1500.
my_account.withdraw(2000) # Output: Insufficient funds.
my_account.withdraw(500) # Output: Withdrew 500. New balance is 1000.

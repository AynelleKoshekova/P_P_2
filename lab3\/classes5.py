class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

    def show_balance(self):
        print(f"{self.owner}'s account balance: {self.balance}")
account = BankAccount("Alice", 1000)  
account.show_balance()  

account.deposit(500)  
account.withdraw(200)   
account.withdraw(2000)  
account.show_balance() 

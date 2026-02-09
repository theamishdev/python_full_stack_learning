class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display(self):
        print(f"\nAccount Holder: {self.name}")
        print(f"Current Balance: {self.__balance}")

if __name__ == "__main__":
    account = Bank("Amish Verma", 1000)
    account.display()
    account.deposit(500)
    account.withdraw(200)

    print(f"Balance using method: {account.get_balance()}")
    
    account.set_balance(5000)
    print(f"Balance after update: {account.get_balance()}")

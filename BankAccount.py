import random
import string
class BankAccount:
    account_num = set()

    def __init__(self, account_holder:int, initial_balance:int=0):
        self.account_holder = account_holder
        self.__balance = 0
        self.deposit(initial_balance)
        self.account_number =  "".join(random.choices(string.digits,k=10))

    def generate_account_number(self):
        while True:
            account_number = random.randint(1000000000, 9999999999)  # 10-digit number
            if account_number not in BankAccount.account_num:
                BankAccount.account_num.add(account_number)
                return account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("Deposit amount must be greater than zero.")
            return self.balance

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                return self.balance
            else:
                print("Insufficient funds.")
                return self.balance
        else:
            print("Withdrawal amount must be greater than zero.")
            return self.balance

    def get_balance(self):
        return self.__balance
    def set_balance(self, balance):
        if not isinstance(balance, int) and balance >= 0:
            raise Exception("balance must be integer and is 0 SAR or more")
        self.__balance = balance
    

    def get_account_holder(self):
        return self.account_holder

    def get_account_number(self):
        return self.account_number
    

    def __str__(self):
        return f"this bank account belongs to {self.get_account_holder()}."
    

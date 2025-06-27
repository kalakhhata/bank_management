from datetime import datetime
class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.__account_number=account_number
        self.account_holder=account_holder
        self.__balance=balance
        self.transactions=[]
    
    def deposit(self,amount):
        self.__balance+=amount
        print(f"${amount} has been deposited")
        self.add_transactions(f"Deposited ${amount}")
    
    def withdraw(self,amount):
        if self.__balance-amount>=0:
            self.__balance-=amount
            print(f"${amount} has been withdrawed")
            self.add_transactions(f"Withdrew ${amount}")
        else:
            print("Not Enough Funds in the Account")

    def get_balance(self):
        return self.__balance
    
    def add_transactions(self,detail):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{timestamp} - {detail}")
    
    def display_transactions(self):
        print(f"\nTransaction History for {self.account_holder}:")
        for t in self.transactions:
            print(t)


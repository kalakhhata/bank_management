from .BankAccount import BankAccount

class Bank:
    def __init__(self):
        self.accounts={}
    
    def create_account(self,account_holder,account_number,deposit=0):
        if account_number in self.accounts:
            print("Account Number Already Taken")
        else:
            account= BankAccount(account_number,account_holder,deposit)
            self.accounts[account_number]= account
            print("Account created Successfully.")
    
    def get_account(self,account_number):
        return self.accounts.get(account_number)

    def display_all_ac(self):
        if not self.accounts:
            print("No Accounts Added")
        else:
            for acc in self.accounts.values():
                acc.display()
    

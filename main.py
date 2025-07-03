from models.Bank import Bank

def show_menu():
    print("\n====== Bank Management System ======")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account Info")
    print("5. Show Transaction History")
    print("6. Display All Accounts")
    print("7. Exit")

def main():
    bank = Bank()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter account number: ")
            acc_no = input("Enter account holder name: ")
            try:
                deposit = float(input("Enter initial deposit amount: "))
                bank.create_account(acc_no, name, deposit)
            except ValueError:
                print("Invalid deposit amount.")

        elif choice == '2':
            acc_no = input("Enter account number: ")
            account = bank.get_account(acc_no)
            if account:
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid amount.")
            else:
                print("Account not found.")

        elif choice == '3':
            acc_no = input("Enter account number: ")
            account = bank.get_account(acc_no)
            if account:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid amount.")
            else:
                print("Account not found.")

        elif choice == '4':
            acc_no = input("Enter account number: ")
            account = bank.get_account(acc_no)
            if account:
                account.display()
            else:
                print("Account not found.")

        elif choice == '5':
            acc_no = input("Enter account number: ")
            account = bank.get_account(acc_no)
            if account:
                print("\n--- Transaction History ---")
                account.display_transactions()
            else:
                print("Account not found.")

        elif choice == '6':
            bank.display_all_ac()

        elif choice == '7':
            print("Thank you for using the Bank Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

# 🔐 Run main() only if the script is executed directly
if __name__ == "__main__":
    main()

#Creating an account
def create_account(accounts):
    owner = input("Enter account owner's name: ")
    if owner in accounts:
        print("Account already exists.")
    else:
        accounts[owner] = 0
        print("Account created.")
#Performing transactions
def perform_transaction(accounts):
    owner = input("Enter account owner's name: ")
    if owner not in accounts:
        print("No account found.")
        return
    transaction_type = input("Enter transaction type (deposit/withdraw): ").lower()
    amount = float(input("Enter amount: "))
    if transaction_type == 'deposit':
        if amount > 0:
            accounts[owner] += amount
            print(f"Deposited ${amount}. New balance: ${accounts[owner]}")
        else:
            print("Amount must be positive.")
    elif transaction_type == 'withdraw':
        if 0 < amount <= accounts[owner]:
            accounts[owner] -= amount
            print(f"Withdrew ${amount}. New balance: ${accounts[owner]}")
        else:
            print("Invalid amount.")
    else:
        print("Invalid transaction type.")
#updating account info
def update_account_info(accounts):
    old_owner = input("Enter current account owner's name: ")
    if old_owner not in accounts:
        print("No account found.")
        return

    new_owner = input("Enter new account owner's name: ")
    if new_owner in accounts:
        print("Account already exists for new owner.")
    else:
        accounts[new_owner] = accounts.pop(old_owner)
        print("Account owner updated.")
#deleting the account
def delete_account(accounts):
    owner = input("Enter account owner's name: ")
    if owner in accounts:
        del accounts[owner]
        print("Account deleted.")
    else:
        print("No account found.")
#seraching account info
def search_account_info(accounts):
    owner = input("Enter account owner's name: ")
    if owner in accounts:
        print(f"Account owner: {owner}, Balance: ${accounts[owner]}")
    else:
        print("No account found.")
#viewing costumer list
def view_customers_list(accounts):
    if accounts:
        print("Customers list:")
        for owner, balance in accounts.items():
            print(f"Owner: {owner}, Balance: ${balance}")
    else:
        print("No accounts found.")

def main():
    accounts = {}
    actions = {
        '1': create_account,
        '2': perform_transaction,
        '3': update_account_info,
        '4': delete_account,
        '5': search_account_info,
        '6': view_customers_list,
        '7': exit
    }

    while True:
        print("\n1. Create Account")
        print("2. Perform Transaction")
        print("3. Update Account Info")
        print("4. Delete Account")
        print("5. Search Account Info")
        print("6. View Customer's List")
        print("7. Exit System")

        choice = input("Enter your choice: ")
        if choice in actions:
            actions[choice](accounts)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

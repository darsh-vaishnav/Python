def check_balance(balance):
    print(f"Your current balance is: ₹{balance}")
    return balance


def credit_balance(balance, amount):
    if amount > 0:
        balance += amount
        print(f"₹{amount} credited successfully.")
        print(f"Updated balance: ₹{balance}")
        return balance
    else:
        print("Invalid amount. Please enter a positive value.")
        return balance


def withdraw_balance(balance, amount):
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Updated balance: ₹{balance}")
            return balance
        else:
            print("Insufficient balance.")
            return balance
    else:
        print("Invalid amount. Please enter a positive value.")
        return balance


balance = 5000

while True:
    print("\nBank Menu")
    print("1. Check Balance")
    print("2. Credit Balance")
    print("3. Withdraw Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        balance = check_balance(balance)
    elif choice == 2:
        amount = int(input("Enter amount to credit: "))
        balance = credit_balance(balance, amount)
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        balance = withdraw_balance(balance, amount)
    elif choice == 4:
        print("Thank you for using the bank service.")
        break
    else:
        print("Invalid choice. Please try again.")
        
balance = 30000

while True:
    print("\n1. Check Balance\n2. Credit\n3. Withdraw\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        check_balance(balance)
    elif choice == 2:
        amount = int(input("Enter amount to credit: "))
        balance = credit_balance(balance, amount)
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        balance = withdraw_balance(balance, amount)
    elif choice == 4:
        print("Thank you")
        break
    else:
        print("Invalid choice")

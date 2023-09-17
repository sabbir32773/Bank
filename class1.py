while True:
    try:
        current_amount = int(input("Enter your current amount: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for the current amount.")

while True:
    print("Do you want to:\n1. Deposit\n2. Withdraw")
    try:
        choice = int(input("Choose an option (1/2): "))
        if choice in [1, 2]:
            break
        print("Invalid choice. Please choose 1 for deposit or 2 for withdrawal.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

while True:
    try:
        amount = (
            int(input("Enter the amount to deposit: "))
            if choice == 1
            else int(input("Enter the amount to withdraw: "))
        )
        if choice == 1:
            current_amount += amount
            print(f"Deposit successful. Your updated balance is: {current_amount}")
        else:
            if amount > current_amount:
                print("Insufficient balance. Withdrawal not allowed.")
            else:
                current_amount -= amount
                print(
                    f"Withdrawal successful. Your updated balance is: {current_amount}"
                )
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for the amount.")

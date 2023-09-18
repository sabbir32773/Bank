def authenticate_user():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == "sabbir32" and password == "Sabbir!!":
            return True

        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Invalid username or password. {remaining_attempts} attempts remaining.")

    print("Too many invalid attempts. Access denied.")
    return False


def calculate_operation(choice):
    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print("Result of addition:", result)
    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print("Result of subtraction:", result)
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print("Result of multiplication:", result)
    elif choice == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result of division:", result)
    elif choice == 5:
        num1 = float(input("Enter the base: "))
        num2 = float(input("Enter the exponent: "))
        result = num1**num2
        print("Result of power:", result)
    else:
        print("Invalid choice. Please choose a valid operation.")


if __name__ == "__main__":
    # Authentication
    if authenticate_user():
        try:
            choice = int(
                input(
                    "What do you want to do? 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Power (1, 2, 3, 4, 5): "
                )
            )
            calculate_operation(choice)
        except ValueError:
            print("Invalid input. Please enter a valid numeric choice.")
    else:
        print("Access denied.")

def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt user to choose an operation
    choice = input("Enter the number corresponding to your choice (1/2/3/4): ")

    # Validate choice
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select a valid operation.")
        return

    try:
        # Prompt user to input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform calculation based on the choice
        if choice == '1':
            result = num1 + num2
            operation = '+'
        elif choice == '2':
            result = num1 - num2
            operation = '-'
        elif choice == '3':
            result = num1 * num2
            operation = '*'
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = '/'

        # Display the result
        print(f"The result of {num1} {operation} {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()

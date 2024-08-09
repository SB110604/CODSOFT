def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operation():
    operations = {
        '1': ('Addition', '+'),
        '2': ('Subtraction', '-'),
        '3': ('Multiplication', '*'),
        '4': ('Division', '/')
    }
    print("\nChoose an operation:")
    for key, (name, symbol) in operations.items():
        print(f"{key}: {name} ({symbol})")
    
    while True:
        choice = input("Enter the number corresponding to the operation: ")
        if choice in operations:
            return operations[choice][1]
        else:
            print("Invalid choice. Please choose a valid operation.")

def perform_calculation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero."
        return num1 / num2

def main():
    print("Welcome to Simple Calculator")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()

    result = perform_calculation(num1, num2, operation)
    print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()

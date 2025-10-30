def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def get_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input, please enter a number.")

def main():
    print("Simple Calculator")
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    while True:
        print("\nAvailable operations: +, -, *, /")
        op = input("Choose an operation or 'q' to quit: ").strip()
        if op == 'q':
            print("Exiting calculator.")
            break
        if op not in operations:
            print("Invalid operation.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        result = operations[op](num1, num2)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()


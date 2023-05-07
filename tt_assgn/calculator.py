def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
    else:
        return a / b


def _get_numbers():
    num1 = (input("Enter first number: "))
    num2 = (input("Enter second number: "))
    assert num1.isnumeric() and num2.isnumeric()
    return float(num1), float(num2)


def menu():
    print("Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        num1, num2 = _get_numbers()
        print("Result:", add(num1, num2))

    elif choice == 2:
        num1, num2 = _get_numbers()
        print("Result:", subtract(num1, num2))

    elif choice == 3:
        num1, num2 = _get_numbers()
        print("Result:", multiply(num1, num2))

    elif choice == 4:
        num1, num2 = _get_numbers()
        print("Result:", divide(num1, num2))

    elif choice == 5:
        exit()

    else:
        print("Invalid choice")




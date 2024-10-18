import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    print("\n" * 2)

    should_accumulate = True

    num1 = float(input("What's the first number?:  "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation = input("Pick an operation:  ")

        while operation not in operations:
            print("Invalid operation! Please choose a valid operation symbol.")

            operation = input("Pick an operation:  ")

        num2 = float(input("What's the next number?:  "))

        result = operations[operation](num1, num2)

        print(f"{num1:.2f} {operation} {num2:.2f} = {result:.2f}")

        y_or_n = input(f"Type 'y' to continue calculating with {result:.2f},\nType 'n' to start a new calculation,\nType 'exit' to exit to calculator\n:   ").lower()

        while not y_or_n in ['y', 'n', 'exit']:
            print("Invalid operation! Please choose a valid operation symbol.")
            y_or_n = input(f"Type 'y' to continue calculating with {result:.2f},\nType 'n' to start a new calculation,\nType 'exit' to exit to calculator\n:   ").lower()

        if y_or_n == 'y':
            num1 = result
        elif y_or_n == 'n':
            should_accumulate = False
            calculator()
        else:
            print("Calculator is off!")
            print("Bye!")
            break



calculator()


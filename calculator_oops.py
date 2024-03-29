class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"


def main():
    calc = Calculator()

    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", calc.add(num1, num2))
            elif choice == '2':
                print("Result:", calc.subtract(num1, num2))
            elif choice == '3':
                print("Result:", calc.multiply(num1, num2))
            elif choice == '4':
                print("Result:", calc.divide(num1, num2))
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()

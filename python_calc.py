# Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Invalid/Math error"
    return x / y

def is_even(n):
    return n % 2 == 0

def percentage(n, p):
    return (n * p) / 100

# Loop
while True:
    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Even or Odd")
    print("6. Percentage")
    print("7. Exit")

    choice = input("Enter choice (1-7): ")

    if choice == "7":
        print("Closing calculator")
        break

    elif choice == "5":
        n = int(input("Enter number: "))
        print("even" if is_even(n) else "odd")

    elif choice == "6":
        n = float(input("Enter number: "))
        p = float(input("Enter percentage: "))
        print("Result:", percentage(n, p))

    elif choice in ["1", "2", "3", "4"]:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(x, y))
        elif choice == "2":
            print("Result:", subtract(x, y))
        elif choice == "3":
            print("Result:", multiply(x, y))
        elif choice == "4":
            print("Result:", divide(x, y))

    else:
        print("Invalid choice")

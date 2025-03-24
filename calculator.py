def calculator():
    a = float(input("Choose first number: "))
    b = float(input("Choose second number: "))
    operation = input("Choose operation: (+, -, *, /): ")

    if operation == "+":
        print(f"Result: {a + b}")
    elif operation == "-":
        print(f"Result: {a - b}")
    elif operation == "*":
        print(f"Result: {a * b}")
    elif operation == "/":
        if b == 0:
            print("Division by zero")
        else:
            print(f"Result:: {a / b}")
    else:
        print("Incorent operation")

calculator()
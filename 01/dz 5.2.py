while True:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    op = input("Enter an operation (+, -, *, /): ")

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b != 0:
            result = a / b
        else:
            print("Error: division by zero")
            continue
    else:
        print("Unknown operation")
        continue

    print("Result:", result)

    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != "y":
        print("Program finished.")
        break
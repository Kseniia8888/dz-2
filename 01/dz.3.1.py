first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result:", first_number + second_number)

elif operation == "-":
    print("Result:", first_number - second_number)

elif operation == "*":
    print("Result:", first_number * second_number)

elif operation == "/":
    if second_number == 0:
        print("Error: division by zero is not allowed")
    else:
        print("Result:", first_number / second_number)

else:
    print("Error: unknown operation6")
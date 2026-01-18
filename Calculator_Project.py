def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def exponent(a, b):
    return a ** b


ip = 1

while ip == 1:
    operation = input("Enter operation to perform (+, -, *, /, **): ")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    if operation == "+":
        result = addition(a, b)
        print(result)
        while True:
            step = input("Do you want to continue with result? (yes/no/x): ").lower()
            if step == "yes":
                c = int(input("Enter the number: "))
                result = addition(result, c)
                print(result)
            elif step == "x":
                ip = 0
                break
            else:
                break

    elif operation == "-":
        result = subtraction(a, b)
        print(result)
        while True:
            step = input("Do you want to continue with result? (yes/no/x): ").lower()
            if step == "yes":
                c = int(input("Enter the number: "))
                result = subtraction(result, c)
                print(result)
            elif step == "x":
                ip = 0
                break
            else:
                break

    elif operation == "*":
        result = multiplication(a, b)
        print(result)
        while True:
            step = input("Do you want to continue with result? (yes/no/x): ").lower()
            if step == "yes":
                c = int(input("Enter the number: "))
                result = multiplication(result, c)
                print(result)
            elif step == "x":
                ip = 0
                break
            else:
                break

    elif operation == "/":
        result = division(a, b)
        print(result)
        while True:
            step = input("Do you want to continue with result? (yes/no/x): ").lower()
            if step == "yes":
                c = int(input("Enter the number: "))
                result = division(result, c)
                print(result)
            elif step == "x":
                ip = 0
                break
            else:
                break

    elif operation == "**":
        result = exponent(a, b)
        print(result)
        while True:
            step = input("Do you want to continue with result? (yes/no/x): ").lower()
            if step == "yes":
                c = int(input("Enter the number: "))
                result = exponent(result, c)
                print(result)
            elif step == "x":
                ip = 0
                break
            else:
                break

    else:
        print("Invalid operation")

    if ip == 1:
        proc = input("Do you want to perform another operation? (yes/no): ").lower()
        if proc != "yes":
            ip = 0

print("Program terminated.")

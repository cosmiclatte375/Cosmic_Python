def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a//b

operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator() :
    number1=int(input("Enter the first number: "))
    for operation in operations_dict:
       print(operation)

    continue_flag=True
    while continue_flag:
        operation=input("Enter the operation: ")
        number2=int(input("Enter the second number: "))
        calculator_function=operations_dict[operation]
        output=calculator_function(number1,number2)
        print(f"The result is {output}")

        should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit: ")
        if should_continue.lower()=="y":
            number1=output
        elif should_continue.lower()=="n":
            continue_flag=False
            calculator()
        else:
            continue_flag=False
            print("Thank you for using this program")

calculator()
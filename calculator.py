def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    else:
        return result

def modulo(x, y):
    try:
        result = x % y
    except ZeroDivisionError:
        return "Cannot perform modulo by zero!"
    else:
        return result

def calculator():
    print("Welcome to Simple Calculator!")
    print("Available operations: +, -, *, /, %")

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print("Result:", add(num1, num2))
    elif operator == '-':
        print("Result:", subtract(num1, num2))
    elif operator == '*':
        print("Result:", multiply(num1, num2))
    elif operator == '/':
        print("Result:", divide(num1, num2))
    elif operator == '%':
        print("Result:", modulo(num1, num2))
    else:
        print("Invalid operator! Please enter one of the provided operators.")

calculator()

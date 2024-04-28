def forward(num):
    return num + 1

def backward(num):
    return num - 1

def horizontal(num1, num2):
    return num1 + num2

def vertical(num1, num2):
    return num1 * num2

def addition(num1, num2):
    return horizontal(num1, num2)

def subtraction(num1, num2):
    return horizontal(num1, -num2)

def multiplication(num1, num2):
    return vertical(num1, num2)

def division(num1, num2):
    if num2 != 0:
        return vertical(num1, 1/num2)
    else:
        return "Error: Division by zero"

# Take input from the user
num = float(input("Enter a number: "))

# Testing the functions
print("Forward of", num, "is", forward(num))
print("Backward of", num, "is", backward(num))
print("Horizontal sum of", num, "and 3 is", horizontal(num, 3))
print("Vertical product of", num, "and 2 is", vertical(num, 2))
print("Addition of", num, "and 2 is", addition(num, 2))
print("Subtraction of", num, "and 2 is", subtraction(num, 2))
print("Multiplication of", num, "and 3 is", multiplication(num, 3))
print("Division of", num, "by 2 is", division(num, 2))

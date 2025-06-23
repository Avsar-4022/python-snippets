# Python program for a simple calculator
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x / y


while True:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(num1, "+", num2, "=", add(num1, num2))
    elif op == "-":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif op == "*":
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif op == "/":
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid operator. Please enter one of the following: +, -, *, /")

    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != "y":
        break

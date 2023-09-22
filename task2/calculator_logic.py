import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def factorial(x):
    if x < 0:
        return "Error: Factorial undefined for negative numbers"
    if x == 0:
        return 1
    return x * factorial(x - 1)

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Square root undefined for negative numbers"
    return math.sqrt(x)

def percentage(x, y):
    return (x * y) / 100

def operate(x, y, operator):
    if operator == '+':
        return add(x, y)
    elif operator == '-':
        return subtract(x, y)
    elif operator == '*':
        return multiply(x, y)
    elif operator == '/':
        return divide(x, y)
    elif operator == '%':
        return percentage(x, y)
    else:
        return "Error: Invalid operator"

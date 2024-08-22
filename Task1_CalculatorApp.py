#
#    Task1_CalculatorApp.py
#
# Created on Fri Aug 23 2024 12:58:00 AM
#       Author: Mina Waguih
#
# Description: A simple calculator app that takes two numbers and an operation
#


def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Invalid operation!")
        return

    print("Result:", result)

calculator()
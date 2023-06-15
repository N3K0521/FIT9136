# Group No:
# Date:
# Description: Simple Calculator

# ask for the operation
operation = input("Please choose the operation: ")

# ask for number 1
number1 = int(input("Please enter the first number: "))

# ask for number 2
number2 = int(input("Please enter the second number: "))

if operation == "+":
    print(str(number1) + " + " + str(number2) + " = " + str(number1+number2))
if operation == "-":
    print(str(number1) + " - " + str(number2) + " = " + str(number1-number2))
if operation == "*":
    print(str(number1) + " * " + str(number2) + " = " + str(number1*number2))
if operation == "/":
    print(str(number1) + " / " + str(number2) + " = " + str(number1/number2))

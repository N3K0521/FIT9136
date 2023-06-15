# Date: 05 March 2022
# Name: FIT9136 Teaching Team
# Description: Simple Calculator

# Define variables for the operands, operator and result; and initialise them with some suitable values.
a = 0
b = 0
op = ""
result = 0

# Prompt for user input for the operator. The input can be add, sub, div, mul.
op = input("Enter operator: ")

# Prompt for user input for both operands. 
a = int(input("Enter operand 1: "))
b = int(input("Enter operand 2: "))

# Apply the operator and store the result in a variable.
if op == "add":
    result = a + b
elif op == "sub":
    result = a - b
elif op == "div":
    result = a // b
elif op == "mul":
    result = a * b
else:
    result = -1
    
# Print the result. 
if result != -1:
    print("The result of " + op + " is " + str(result))
else:
    print("Invalid operator!")

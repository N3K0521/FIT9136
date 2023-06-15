# Group No:
# Date:
# Description: Checking if the string is Palindrome

# Receiving input string
input_str = input("Please insert a string: ")

# Store the string to true -> assuming the string is a Palindrome
palindrome = True

# split the string into half
for char in range(0, int(len(input_str))//2):
    # compare the first half and the inversed second half
    if input_str[char] != input_str[len(input_str)-char-1]:
        palindrome = False
        break

# check if palindrom is True or False
if palindrome is True:
    print("The word " + input_str + " is a palindrome.")
else:
    print("The word " + input_str + " is not a palindrome.")

# Group No:
# Date:
# Description: Checking if the string is Palindrome

# Prompt user for string input 
myString = input("Please enter your string: ")

#get the lenght of the string
lenStr = len(myString)

# assume it is a palindrome
palindrome = True 

#Navigate half of the string (i.e., start from index 0 and end in mid index)
for i in range(0,int(lenStr/2)):
    if myString[i] != myString[lenStr-i-1]: # compare the corresponding letters
        palindrome = False #no, it is not...
        break
        
if palindrome:
    print('The string is a palindrome.')
else:
    print('The string is not a palindrome.')

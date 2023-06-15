# Group No:
# Date:
# Description: Guess my number

#import Python random module
import random
randomNum = random.randint(1, 10)

guess = input("Guess my number: ")

if randomNum == guess:
    print("Your guess is true! My number is " + str(randomNum) )
else:
    print("Your guess is wrong! My number is " + str(randomNum))

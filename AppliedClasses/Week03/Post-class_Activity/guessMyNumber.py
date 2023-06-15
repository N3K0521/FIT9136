# Group No:
# Date:
# Description: Guess my number

#import Python random module
import random

running = True

while running:
    # generate a target random number from 0 to 10.
    number = random.randint(0,10)

    while True:
        user_input = int(input("Please insert a number: "))
        if number == user_input:
            print("Congratulations! You are correct!")
            newgame = input("Do you want to play again? (Input Y/N): ")
            if newgame == "Y":
                break
            else:
                print("GOODBYE")
                running = False
                break
        elif number != user_input:
            print("Try again!")




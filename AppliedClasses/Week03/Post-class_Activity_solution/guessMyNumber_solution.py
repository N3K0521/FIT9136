# Date: 05 March 2022
# Name: FIT9136 Teaching Team
# Description: Guess my number

#import Python random module
import random
# generate a target random number from 0 to 10.
# number = random.randint(0,10)

# a flag shows weather the game is over.
running = True

# a while loop starting next game
while running:
    print('------------Staring a guessing game------------')
    
    # generate a target random number from 0 to 10.
    number = random.randint(0,10)
    
    # a while loop asking user to continuely guess the number
    while True:
        guess = input('Please enter an integer : ')
        # check user input is a digit
        if guess.isdigit():
            # convert the input to an integer
            guess = int(guess)

            """if guess number is target number, print Congratulations,
                then ask user to play next game or not"""

            if guess == number:
                print('Congratulations, you guessed it.')
                newGame = input("Do you Want to play new Game (Y/N)? ")
                if newGame.upper() == 'Y':
                    break
                else:
                    print("GOODBYE")
                    running = False # make the flag to Flase to quit while loop
                    break
            # if it is less than target, print...
            elif guess < number:
                print('No, it is a little higher than that.')
            # if it is greater than target, print..
            else:
                print('No, it is a little lower than that.')
        # if the input is invalid, print...
        else:
            print('You will need to enter a valid integer!') 

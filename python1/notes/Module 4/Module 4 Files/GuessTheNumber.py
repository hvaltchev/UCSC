# guess the number

import random    # include everything in the 'random' module
MAXIMUM_GUESSES = 5

#Show introduction
print('Welcome to my guess the number program.')
print('Guess my number between 1 and 20.')
print('You have', MAXIMUM_GUESSES, 'guesses.')
print

def playOneRound():
    # Choose a random target
    target = random.randrange(1, 21)
    # Initialize a counter
    guessCounter = 0  #  keeps track of the number of guesses

    while True:
        #Ask the user for a guess
        userGuess = input('Take a guess: ')  #prompt the user to enter a number
        userGuess = int(userGuess)   # convert the characters to an integer
        # Increment the guess counter
        guessCounter = guessCounter + 1

        # If  user's guess is correct, we're done
        if userGuess == target:
            print('You got it in', guessCounter, 'guesses')
            break   #exit the loop now

        # if user's guess is too low, tell the user
        elif userGuess < target:
            print('Your guess is too low')

        # if user's guess is too high, tell the user
        else:
            print('Your guess is too high')

        # If reached max guesses, tell answer, we're done
        if guessCounter == MAXIMUM_GUESSES:
            print("You didn't get it in", MAXIMUM_GUESSES, "guesses - loser!")
            print('The correct answer was:', target)
            break



while True:
    playOneRound()
    print
    goAgain = input('Play again? Press y to continue or press ENTER to quit.')
    if goAgain == '':
        break

print
print('OK, thanks for playing.')


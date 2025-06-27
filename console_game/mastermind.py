# In this game, the computer will set up a multi-digit number, and the player will try to guess the
# number. After each guess, the computer will reveal how many digits were exactly correct and how many
# digits in the number but are not in the correct position.

# Import the random module, see https://www.geeksforgeeks.org/python-random-function/ for more info.
# Alternatively, you can use the "from random import randint" to just get random.

# We define a constant for the number of digits.
DIGITS = 5
class MastermindGame():
    def __init__(self, digits):
        # A parameter to check if a guess completes the game.
        self._complete = False
        # TODO: Create the hidden number, based on the number of digits

    # Return True if the game is complete, False otherwise
    def is_complete(self):
        # TODO: Complete function
        pass

    def guess(self, guess):
        # TODO: Check to make sure that the guess has the correct number of digits
        correct = 0
        incorrect = 0

        # TODO: Check to see if the guess is exactly correct, and set the game to complete if the player
        # guesses the hidden number

        # TODO: Find how many digits in the guess are in the correct position. You can loop over all the digits
        # to check

        # TODO: Figure out how many digits in the guess are in the hidden number. You can do this by looping
        # over all the digits from 0 - 9, see how many of those are in the hidden number, how many of those
        # are in the guess, and take the lesser of these two quantities. The incorrect position numbers should be the
        # difference between the number of common digits in the previous step and the number of digits in the correct
        # position.

        return correct, incorrect

quit_playing = False
current_game = None
while True: # TODO: Change this loop so that we stop playing if the player quits
    pass
    # TDDO: If there is no game or the game is complete, create a new game.

    # TODO: Ask the player for a guess.

    # TODO: Call the guess() function for the game and print out to the user the response of how many
    # digits are in the right position and how many digits are in the hidden number but in the
    # incorrect position.

    # TODO: Check to see if the game is complete. If the game is complete, display the result and the hidden number,
    # and ask the player if they want to play again.
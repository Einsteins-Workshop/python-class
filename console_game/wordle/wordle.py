from rich.console import Console
from rich.theme import Theme
from string import ascii_letters

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

CORRECT_LETTER = 1
LETTER_IN_WORD = 2
LETTER_NOT_IN_WORD = 3
NOT_LETTER = 4

def main():
    word = get_random_word()

    # TODO: Define a constant with maximum number of guesses, and create an array with that number.
    # of guesses with all underlines instead of the one in the current guesses variable.
    guesses = ["_____"]

    try:
        # TODO: Define a constant with maximum number of guesses, and loop idx for the number of times
        # of the guesses to get a word.
        idx = 0

        # TODO: Define a variable for the state of the game, which can be WIN, LOSS, or GUESS. Create a loop, which
        #  should continue as long as the state is GUESS.

        # TODO: Check to see the state of the game.  If the user guessed the word correctly, update the title
        #  to show that the user won. If the user has guessed six time and failed to guess the word, update the title
        # to show that the user lost.  Otherwise, change the title to reflect the guess that they are currently on.
        # make sure to change the state variable appropriately.
        print_title("Guess 1")

        show_guesses(guesses, word)

        # TODO: only call guess_word if the user is still in guess mode.  Make sure to change the idx appropriately.
        guesses[idx] = guess_word(guesses)

    # If the user exits the program with control-C, skip the error and go to game over.
    except KeyboardInterrupt:
        pass

def get_random_word():
    # TODO: The guessable words are in the guess_words.txt file.  Read the file in and select a
    # random word from the file. For consistency, make sure to capitalize the word.
    return "SHADY"

def show_guesses(guesses, word):
    for guess in guesses:
        # TODO replace the print below with console printing
        styled_guess = []
        for letter, correct in zip(guess, word):
        #   TODO: compare letter (the letter in guess) to correct (the correct letter), and if not the
        #       same, see if letter is in the word.  Use console_guess_styling to get the correct status, be sure to
        #       replace CORRECT_LETTER in the line below.
            style = console_guess_styling(CORRECT_LETTER)
            letter_to_print = f"[{style}]{letter}[/]"
            styled_guess.append(letter_to_print)
        #   TODO: Keep track, for all guesses (so outside of the guesses loop) of what letters have
        #       been guessed.  Make sure to keep the most accurate value for the letter
        console.print("".join(styled_guess), justify="center")
    # TODO: Print out all letters, with each letter having a style as follows: if the letter is guessed and is in a=
    # correct position, use CORRECT_LETTER.  If the letter is guessed and is in the word but is not in any correct
    # position in any of the guesses, use LETTER_IN_WORD.  If the letter is guessed but not in word, use
    # LETTER_NOT_IN_WORD. Otherwise, use NOT_LETTER styling.

def console_guess_styling(status):
    style = "dim"
    if status == CORRECT_LETTER:
        style = "bold white on green"
    elif status == LETTER_IN_WORD:
        style = "bold white on yellow"
    elif status == LETTER_NOT_IN_WORD:
        style = "white on #666666"
    return style

def guess_word(previous_guesses):
    # TODO: Show an appropriate
    guess = console.input()

    # TODO: Check to make sure that new guess is not an already guess word. If so, print out a warning
    # and get another guess from the user (easiest is to recursively call guess_word)
    #console.print(f"You've already guessed {guess}.", style="warning")

    # TODO: Check to make sure that the guess has the correct number of letters. If so, print out a warning
    # and get another guess from the user.

    # TODO: check to make sure that all letters are in ascii_letters. If not, print out a warning
    # and get another guess from the user

    return guess

def print_title(title):
    # TODO: Add rich styling, here is an example
    console.clear()
    console.rule(f"[blue]:leafy_green: {title} :leafy_green:[/]\n")


if __name__ == "__main__":
    main()
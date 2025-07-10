# Code taken from https://github.com/kcxt/Hangman/
# Word list from https://github.com/Vickyabiodun/Hangman-Game/blob/main/hangman_words.py

from random import randint as random
import random

# Get the words
def get_all_words():
    words = open("words.txt", "r").readlines()

    # This removes all but the last letter, which is a newline.
    for i in range(len(words)):
        words[i] = words[i][:-1]
    return words

stages  = ['''






 =========''', '''


       |
       |
       |
       |
       |
 =========''', '''

    +---+
       |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|-  |
       |
       |
 =========''', '''


   +---+
   |   |
   O   |
  /|-  |
  /    |
       |

=========''', '''

   +---+
   |   |
   O   |
  /|-  |
  / |  |
       |
=========''']


# Runs the program
print("MAIN")
wrong = ""
print("/*******\\ ")
print("|HANGMAN|")
print("\\*******/")

all_words = get_all_words()
incorrect_letters = 0

# Step 1:  Choose one word from the list of all words. You'll want to find an appropriate
# function from the random module.  Try searching online.
word = random.choice(all_words)
guessed_letters = ['a', 'e', 'i', 'o', 'u']


while True:


       #print("WINNER!")
        #print("!!"+"!"*len(word))
        #print("!"+word+"!")
       #print("!!"+"!"*len(word))


    print(stages[incorrect_letters])

    # Step 2: Print the length of the word
    print("Length:" + str(len(word)))

    # Step 3: Print the word. Use an _ for each letter that has not yet been
    # guessed successfully.

    for letter in word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print("\n")

    # Step 4: Print the guessed letters.
    #print("Guessed letters: ???"+wrong)

    # Step 5: Ask the player for a letter.
    letter = 'a'
    choice_letter = input("What letter do you chose?")
    # Step 6: If the letter has already been asked (or is not a valid letter) tell
    # them that they are being naughty.
    if letter == "!":
        print("Insert message for invalid letter here")
    elif letter == "z":
        print("Insert message for repated letter here")
    else:
        # Step 7: Add the letter to guessed_letters

        # Step 8: Check to see if the letter is in the word. If it is, let the player know
        print("Maybe I should check to see whether the player's letter is in the word and, if so, let them know it is correct")

            # Step 9: If the player's letter is in the word, check to see if they have guessed all the letters.
            # If so, declare them the winner and make sure that we end the loop.

        # Step 10: If the player's letter is not in the word, let them know. and make sure
        # to keep track of how many they got wrong

            # Step 11: If the player has too many wrong (more than the number of stages), show
            # them the lose screen and make sure to end the loop
    print("You lose")
    print("      \\            /      ")
    print("   _   \\          /   _   ")
    print("  | |   \\        /   | |  ")
    print("   -                  -   ")
    print("                          ")
    print("       ____________       ")
    print("      /            \\      ")
    break

    print("\n"*100)

# Step 12: No matter what, at game's end, print out the word

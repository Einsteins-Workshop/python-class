# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("system")
define M = Character("Mage")
define Dm = Character("Dark Mage")
define K = Character("Knight")
define Dk = Character("Dark Knight")
define A = Character("Assassin")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg cave

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show system cat :
        xalign 0.1, yalign 0.2

    # These display lines of dialogue.

    s "Hi! I'm your system. I'm going to be helping you today!"

    s "In this game you are going to be selecting a type of Warrior class!"

    s "You can be a Mage, a Dark Mage, Healer, a Knight, a Dark Knight or a Assassin"

    show mage :
        xalign 0.5, yalign 0.5

    s "If your a mage then your powers are: Arcane energy level: 10, Elemental forces level: 10, reality-altering spells level: 10, Defense level: 6"

    show Dark_mage :
        xalign 0.5, yalign 0.5

    s "If your a Dark mage then your powers are: Necromancy level: 10, Shadow & Chaos Magic level: 10, Curses level: 10, Summoning level: 10"

    # This ends the game.

    return
what = input("What is your name?: ")

def ask_age():
    print("Hi", what)
    what1 = input("What do you do?: ")
    if (what1 == "nothing"):
        print("That is so boring.")
    if (what1 == "fencing"):
        print("Cool!!!")
    if (what1 != "nothing" or "fencing"):
        print("oh.")
    old = input("How old are you?: ")
    if (old == "0"):
        print("Then you've not been born.")
    if (old >= "90"):
        print("Wow your old.")
    if (old != "0" or "90"):
        print("cool")
    print("Your name is", what, ",you do", what1, "and you are", old, "years old!")


if what.isnumeric():
        what = input("Please wright your name in letters: ")
        ask_age()

else:
    ask_age()

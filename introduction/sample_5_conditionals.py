what = input("What is your name?: ")
if what.isnumeric():
        what = input("Please wright your name in letters: ")
        print("Hi", what)
        what1 = input("What do you do?: ")
        if (what1 == "nothing"):
            print("That is so boring.")
        if (what1 == "fencing"):
            print("Cool!!!")
        if (what1 != "nothing" or "fencing"):
            print("oh.")
        old = input("How old are you?: ")
        if (old =="0"):
            print("Then you've not been born.")
        if (old >="90"):
            print("Wow your old.")
        if (old != "0" or "90"):
            print("cool")
else:
    print("Hi", what)
    what1 = input("What do you do?: ")
    if (what1 == "nothing"):
        print("That is so boring.")
    if (what1 == "fencing"):
        print("Cool!!!")
    if (what1 != "nothing" or "fencing"):
        print("oh.")
    age = input("How old are you?:")
    if (age =="0"):
        print("Then you've not been born.")
    if (age >="90"):
        print("Wow your old.")
    if (age != "0" or "90"):
        print("cool")

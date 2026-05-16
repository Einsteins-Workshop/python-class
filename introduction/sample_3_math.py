def did_you_die():
    print("You wake in a world with no color. You look around and see that you are on a path.")
    lost = input("You can go left(1) or right(2). Enter here: ")
    print("Oh you did option" ,lost, ". Sorry but no mater what you piked you can only go left.")
    print("You walk for a long time, then you go to sleep.")
    print("When you wake you find your self in a new world. This world has blue grass and a green sky.")
    print("You can see two doors in the air. The left is made of gold and the right is made of wood.")
    doors = input("You can go in a door. Do you take the left door(1) or do you take the right(2). Enter here: ")
    if (doors == "1"):
        print("You try to open the gold door but you can't so you go through the wood door.")
        print("You walk through the wood door then you find you self back at your house")
        print("YOU WIN!!")
    if (doors == "2"):
        print("You walk through the wood door then you find you self back at your house")
        print("YOU WIN!!")

name = input("What is the name you would like to have for this game? Enter here: ")

print("Hello", name, "I think you will have fun with this so lets get started!!")
print("Just a warning you can not go back after you pick what to do!!")
print("   ")
print("It's a dark and stormy night and you find your self in the woods on a path!")

start = input("You can go left(1) or right(2)! Enter your choice here: ")

if(start == "1"):
    print("You start going left and you find a cave. you enter the cave and find a dragon next to you.")
    dragon = input("There is a bow on the ground. Do you try to kill the dragon with the bow(1) or do you wake the dragon to make a deal(2). Enter here: ")
    if(dragon == "1"):
        print("You fire the bow but it bounces of the dragon. Now the dragon is angry and has eaten you.")
        print("The end")
        did_you_die()
    if(dragon == "2"):
        print("Dragon is grumpy after you wake it. And now it has eaten you.")
        print("The end")
        did_you_die()

if(start == "2"):
    print("You travel for hours then you find a meadow with red flowers on the right")
    flowers = input("Do you enter the meadow(1) or do you keep going(2). Enter here: ")
    if(flowers == "1"):
        print("The flowers put you to sleep for the rest of time.")
        print("The end")
        did_you_die()
    if(flowers == "2"):
        print("You keep walking until you find a house")
        house = input("Do you go into the house(1) or not(2). Enter here: ")
        if(house == "1"):
            print("You Enter the house and the door slams behind you. You are trapped!")
            print("The end")
            did_you_die()
        if(house == "2"):
            print("You keep going then you see a window in the air next to a pine tree.")
            window = input("Do you go in the window(1) or do you keep going(2)? Enter here: ")
            if(window == "2"):
                print("You walk past the window then the pine tree falls on you.")
                print("The end")
                did_you_die()
            if(window == "1"):
                print("You find your self in a new world. This world has blue grass and a green sky.")
                print("You can see two doors in the air. The left is made of gold and the right is made of wood.")
                doors = input("You can go in a door. Do you take the left door(1) or do you take the right(2). Enter here: ")
                if(doors == "1"):
                    print("You walk through the gold door into darkness then you find your self falling into a volcano.")
                    print("The end")
                    did_you_die()
                if(doors == "2"):
                    print("You walk through the wood door then you find you self back at your house")
                    print("YOU WIN!!")
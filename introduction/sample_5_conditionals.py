def back_back():
    mmove = ["north", "south", "east", "west", "up", "down"]
    mnext_move = ["north", "south", "east", "west", "up", "down"]
    mmovee = input("Your in a forest you can go north, south, east or west: ")
    mgo = mmovee
    mnext_one = next_move[move.index(mgo)]
    if (next_one == "north"):
        mmovee1 = input("You go north. Now you are at a river you can go north, south, east or west: ")
        mgo1 = mmovee1
        mnext_one1 = mnext_move[mmove.index(mgo1)]
        if (mnext_one1 == "north"):
            print("sorry you drowned")
    if (mnext_one == "south"):
        mmovee2 = input("You go south. Now you are at a big pit, you can go down or north: ")
        mgo2 = mmovee2
        mnext_one2 = mnext_move[mmove.index(mgo2)]
        if (mnext_one2 == "down"):
            print("Sorry you lost your grip and fell")

Hi = input("hi what is your name: ")
print("Hi", Hi)
print("Ok, lets go!!")
move = ["north", "south", "east", "west", "up", "down"]
next_move = ["north", "south", "east", "west", "up", "down"]
movee = input("Your in a forest you can go north, south, east or west: ")
go= movee
next_one = next_move[move.index(go)]
if(next_one == "north"):
    movee1 = input("You go north. Now you are at a river you can go north, south, east or west: ")
    go1 = movee1
    next_one1 = next_move[move.index(go1)]
    if(next_one1 == "north"):
        print("sorry you drowned")
    if(next_one1 == "south"):
        back_back()
if(next_one == "south"):
    movee2 = input("You go south. Now you are at a big pit, you can go down or north: ")
    go2= movee2
    next_one2 = next_move[move.index(go2)]
    if(next_one2 == "down"):
        print("Sorry you lost your grip and fell")
#if(next_one == "east"):
#    movee3 = input("You go east. Now you are at: ")
#if(next_one == "west"):
#    movee1 = input("You go west. Now you are at: ")

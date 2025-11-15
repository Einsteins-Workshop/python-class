name = input("What is your name: ")

print("Hi", name, "are you ready to play? Ok then lets go!")

# locations
#player = {
#    'name': name,
#    'have_sword': False
#}

#print("You pick up a sword")
#player['have_sword'] = True
def north_north():
    print("You go north. And you are at a river.")
    eastp = input("You can go east, west, north or south: ")
    if (eastp == "east"):
        print("You go east. You die 💀")
    if (eastp == "west"):
        Start_Start()
    if (eastp == "north"):
        print("You go north and you find a dragon. You die 💀")
    if (eastp == "south"):
        uppp = input("You go south. You are in a cave, you can go up or north")
        if (uppp == "up"):
            downp = input("You go up and find a second cave. You can go west or down: ")
            if (downp == "down"):
                down_down()
            if (downp == "west"):
                print("You found the exit. You live")
                print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
                print("😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆")
        if (uppp == "north"):
            north_north()
def down_down():
    uppx = input("You go down. You are in a cave, you can go up or north")
    if (uppx == "up"):
        downx = input("You go up and find a second cave. You can go west or down: ")
        if (downx == "down"):
            down_down()
        if (downx == "west"):
            print("You found the exit. You live")
            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
            print("😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆")
    if (uppx == "north"):
        north_north()
def ask_ask():
    print("You go east. And you are at a river.")
    east = input("You can go east, west, north or south: ")
    if (east == "east"):
        print("You go east. You die 💀")
    if (east == "west"):
        Start_Start()
    if (east == "north"):
        print("You go north and you find a dragon. You die 💀")
    if (east == "south"):
        up = input("You go south. You are in a cave, you can go up or north: ")
        if (up == "up"):
            down = input("You go up and find a second cave. You can go west or down: ")
            if (down == "down"):
                down_down()
            if (down == "west"):
                print("You found the exit. You live")
                print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
                print("😆😆😆😆😆😆😆😆😆😆😆😆😆😆😆")
        if (up == "north"):
            north_north()


def Start_Start():
    start = input("You are in a forest at night. You can go east or west: ")
    if (start == "east"):
        ask_ask()
    if (start == "west"):
        west = input("You go west. And you are at a cliff, you can go east: ")
        west2 = input("You go east. You are in a forest at night. You can go east: ")
        ask_ask()
Start_Start()
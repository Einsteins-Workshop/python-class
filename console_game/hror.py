 import random
import time

# Player stats
player = {
    "health": 100,
    "inventory": [],
    "alive": True
}

# Possible rooms and events
rooms = [
    "a dark hallway",
    "an old library",
    "a dusty bedroom",
    "a locked basement",
    "a bloodstained kitchen",
    "a cold bathroom"
]

events = [
    "monster_attack",
    "trap",
    "find_item",
    "safe_room"
]

items = ["flashlight", "medkit", "rusty key", "holy water", "knife"]

# Functions
def intro():
    print("🌒 You wake up in a creepy, abandoned mansion...")
    time.sleep(1)
    print("You must survive and find a way out.\n")
    time.sleep(1)

def monster_attack():
    print("😱 A MONSTER jumps out!")
    if "knife" in player["inventory"]:
        print("You fight it off with your knife!")
        damage = random.randint(5, 15)
    else:
        print("You have nothing to defend yourself!")
        damage = random.randint(20, 40)
    player["health"] -= damage
    print(f"You took {damage} damage. Health is now {player['health']}.")

def trap():
    print("🕸️ You triggered a hidden trap!")
    damage = random.randint(10, 30)
    player["health"] -= damage
    print(f"You took {damage} damage. Health is now {player['health']}.")

def find_item():
    item = random.choice(items)
    print(f"✨ You found a {item}!")
    player["inventory"].append(item)

def safe_room():
    print("🔒 You found a quiet, safe room.")
    if "medkit" in player["inventory"]:
        print("You used a medkit to heal.")
        heal = random.randint(15, 30)
        player["health"] += heal
        player["inventory"].remove("medkit")
        print(f"You healed {heal} HP. Health is now {player['health']}.")
    else:
        print("You rest for a bit. Health slightly recovered.")
        player["health"] += 5

def play_turn():
    room = random.choice(rooms)
    print(f"\nYou enter {room}...")
    time.sleep(1)
    event = random.choice(events)
    if event == "monster_attack":
        monster_attack()
    elif event == "trap":
        trap()
    elif event == "find_item":
        find_item()
    elif event == "safe_room":
        safe_room()

    # Check health
    if player["health"] <= 0:
        player["alive"] = False
        print("\n💀 You succumbed to your injuries...")
    else:
        print(f"Inventory: {player['inventory']}")

def game_loop():
    intro()
    while player["alive"]:
        input("\nPress [ENTER] to explore...")
        play_turn()

    print("\n🩸 GAME OVER. You did not survive the haunted house.")

# Start game
game_loop()


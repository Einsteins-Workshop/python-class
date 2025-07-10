# fnaf_console.py
import time
import random
import os

# Game state
power = 100
hours_passed = 0
seconds = 0
doors = {"left": False, "right": False}
camera = False
animatronics = {"Bonnie": 0, "Chica": 0, "Freddy": 0}
game_over = False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_time_str():
    hour_display = 12 + hours_passed
    if hour_display > 12:
        hour_display -= 12
    return f"{hour_display}:00 AM" if hours_passed < 6 else "6:00 AM"

def show_status():
    clear()
    print(f"Time: {get_time_str()}")
    print(f"Power: {power}%")
    print(f"Left Door: {'Closed' if doors['left'] else 'Open'}")
    print(f"Right Door: {'Closed' if doors['right'] else 'Open'}")
    print(f"Camera: {'On' if camera else 'Off'}")
    print("Animatronic Positions:")
    for name, pos in animatronics.items():
        print(f"  {name}: Stage {pos}")
    print("\nCommands: camera, door left, door right, wait, quit")

def update_power():
    global power
    usage = 1
    if doors["left"]: usage += 1
    if doors["right"]: usage += 1
    if camera: usage += 1
    power -= usage
    if power < 0:
        power = 0

def update_time():
    global seconds, hours_passed
    seconds += 15
    if seconds >= 60:
        seconds = 0
        hours_passed += 1
    return hours_passed >= 6

def move_animatronics():
    for name in animatronics:
        if random.random() < 0.25:  # 25% chance to move
            animatronics[name] += 1
            if animatronics[name] > 3:
                animatronics[name] = 3

def check_doors():
    global game_over
    for name, pos in animatronics.items():
        if pos == 3:
            if name == "Bonnie" and not doors["left"]:
                game_over = True
            if name == "Chica" and not doors["right"]:
                game_over = True
            if name == "Freddy" and not (doors["left"] or doors["right"]):
                game_over = True

def main_loop():
    global camera, game_over

    while not game_over:
        show_status()

        if power <= 0:
            print("\nPower has run out! Freddy attacks...")
            time.sleep(2)
            game_over = True
            break

        command = input("\n> ").strip().lower()

        if command == "camera":
            camera = not camera
        elif command == "door left":
            doors["left"] = not doors["left"]
        elif command == "door right":
            doors["right"] = not doors["right"]
        elif command == "wait":
            update_power()
            move_animatronics()
            if update_time():
                print("\nYou survived until 6 AM! 🎉")
                return
            check_doors()
            time.sleep(1)
        elif command == "quit":
            print("Game exited.")
            return
        else:
            print("Invalid command!")

    if game_over:
        print("\nJumpscare! You were caught by an animatronic! 💀")

if __name__ == "__main__":
    main_loop()

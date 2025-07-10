import time
import random
import os

# Game constants
HOURS = ["12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM"]
NIGHT_DURATION = 90  # total seconds for one night
STEP_PER_HOUR = NIGHT_DURATION / 6

# Clear console for better UX
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Game state
class FNAFGame:
    def __init__(self):
        self.power = 100
        self.hour_index = 0
        self.left_door = False
        self.right_door = False
        self.bonnie_pos = 0  # 0 (stage) → 4 (office)
        self.dead = False
        self.start_time = time.time()
        self.last_hour = time.time()
        self.last_bonnie_move = time.time()

    def use_power(self):
        usage = 1  # baseline usage
        if self.left_door:
            usage += 1
        if self.right_door:
            usage += 1
        self.power -= usage
        if self.power <= 0:
            self.dead = True
            print("\n⚡ You ran out of power... The office goes dark...")
            time.sleep(3)
            print("👁️ Glowing eyes appear in the doorway...")
            time.sleep(2)
            print("💀 YOU GOT JUMPSCARED!")
        return usage

    def maybe_move_bonnie(self):
        if time.time() - self.last_bonnie_move > random.randint(5, 10):
            if self.bonnie_pos < 4 and random.random() < 0.6:
                self.bonnie_pos += 1
                print(f"\n👣 You hear footsteps... Bonnie is closer! (Position {self.bonnie_pos})")
                if self.bonnie_pos == 4:
                    if not self.left_door:
                        self.dead = True
                        print("\n🚪 Bonnie entered your office...")
                        time.sleep(1)
                        print("💀 JUMPSCARE! YOU DIED.")
                    else:
                        print("🔒 Bonnie tried to enter, but the left door was shut.")
                        self.bonnie_pos = 0
            self.last_bonnie_move = time.time()

    def maybe_advance_hour(self):
        if time.time() - self.last_hour >= STEP_PER_HOUR:
            self.hour_index += 1
            self.last_hour = time.time()
            if self.hour_index < 6:
                print(f"\n⏰ It's now {HOURS[self.hour_index]}!")

    def show_status(self):
        print(f"\n⏳ Time: {HOURS[self.hour_index]}")
        print(f"🔋 Power: {self.power}%")
        print(f"🚪 Left Door: {'Closed' if self.left_door else 'Open'}")
        print(f"🚪 Right Door: {'Closed' if self.right_door else 'Open'}")
        print(f"🎭 Bonnie Position: {self.bonnie_pos} (Closer as number increases)")

    def input_action(self):
        print("\nOptions: [check] [left door] [right door] [wait]")
        cmd = input(">> ").strip().lower()
        if cmd == "check":
            print(f"👀 You check the cameras... Bonnie is at position {self.bonnie_pos}.")
        elif cmd == "left door":
            self.left_door = not self.left_door
            print("🔒 Left Door Toggled:", "Closed" if self.left_door else "Open")
        elif cmd == "right door":
            self.right_door = not self.right_door
            print("🔒 Right Door Toggled:", "Closed" if self.right_door else "Open")
        elif cmd == "wait":
            print("⏳ Waiting silently...")
        else:
            print("❌ Invalid command.")

# Main game loop
def run_fnaf():
    clear()
    print("🎮 Five Nights at Freddy's (Console Edition)")
    print("Survive until 6 AM. Use power wisely and close doors when needed.\n")
    input("Press ENTER to begin Night 1...")

    game = FNAFGame()

    while not game.dead and game.hour_index < 6:
        clear()
        game.use_power()
        game.maybe_advance_hour()
        game.maybe_move_bonnie()
        game.show_status()
        game.input_action()
        time.sleep(1)

    if not game.dead:
        print("\n🌞 6 AM has arrived!")
        print("🎉 You survived the night!")
    print("\nGame Over.")

if __name__ == "__main__":
    run_fnaf()

import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII visuals
player_tile = r"""
 ________
|        |
|   🟥   |
|________|
You: Throwing tile
"""

opponent_tile = r"""
 ________
|        |
|   🟦   |
|________|
Opponent: On the ground
"""

def ddakji_game():
    clear()
    print("=== 🎴 Squid Game: Ddakji Challenge ===\n")
    print("You have 3 chances to flip the opponent's tile.\n")
    print(player_tile)
    print(opponent_tile)
    input("Press Enter to start...")

    chances = 3
    for attempt in range(1, chances + 1):
        clear()
        print(f"Attempt {attempt} of {chances}")
        print("Get ready...")

        wait_time = random.uniform(1.5, 3.5)
        time.sleep(wait_time)

        print("\nNOW! Slam your tile! (Press 's')")
        start_time = time.time()
        key = input().strip().lower()
        reaction = time.time() - start_time

        if key != 's':
            print("❌ Wrong key! Missed your chance.")
        elif reaction > 1.0:
            print(f"⌛ Too slow! ({reaction:.2f}s)")
        else:
            flip_chance = random.randint(1, 3)
            if flip_chance == 1:
                print("\n💥 SLAM! You flipped the tile!")
                print("🎉 YOU WIN THE DDAKJI CHALLENGE!")
                return
            else:
                print("\n💢 You hit it, but not hard/lucky enough. Try again.")

        time.sleep(1.5)

    print("\n💀 You failed to flip the opponent’s tile.")
    print("❌ GAME OVER.")

if __name__ == "__main__":
    ddakji_game()

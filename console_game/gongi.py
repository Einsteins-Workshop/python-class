import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_gongi_hand(stones_held, stones_on_ground):
    print("\nYour hand: " + "🪨" * stones_held)
    print("Stones on ground: " + "🪨" * stones_on_ground + "\n")

def gongi_game():
    clear()
    print("=== 🪨 Gongi – Squid Game Style ===")
    print("Pick up stones (press 'p') and toss them with timing (press 't').")
    print("Try to catch as many as possible! 5 stones total.\n")
    input("Press Enter to start...")

    stones_on_ground = 5
    stones_held = 0
    score = 0

    while stones_on_ground > 0 or stones_held > 0:
        clear()
        print_gongi_hand(stones_held, stones_on_ground)

        if stones_held == 0 and stones_on_ground > 0:
            print("Pick up a stone! Press 'p'")
            action = input(">> ").lower()
            if action == 'p':
                stones_held += 1
                stones_on_ground -= 1
                print("You picked up a stone.")
            else:
                print("Wrong key! Missed your chance.")
            time.sleep(1)
        elif stones_held > 0:
            print("Toss the stone! Press 't' at the right time!")
            wait_time = random.uniform(1.5, 3)
            print("Get ready...")
            time.sleep(wait_time)
            print("NOW! Press 't' to toss.")
            start_time = time.time()
            action = input(">> ").lower()
            reaction = time.time() - start_time

            if action != 't':
                print("❌ You missed the toss!")
                stones_held -= 1
            elif reaction > 1.0:
                print(f"⌛ Too slow! ({reaction:.2f}s) Stone lost.")
                stones_held -= 1
            else:
                print("✅ Perfect toss!")
                score += 1
                stones_held -= 1
            time.sleep(1)
        else:
            break

    clear()
    print("Game Over!")
    print(f"You scored {score} out of 5 stones.")
    if score == 5:
        print("🔥 Amazing! Gongi Master!")
    elif score >= 3:
        print("👍 Not bad! You passed.")
    else:
        print("😞 Try again to improve your skill.")

if __name__ == "__main__":
    gongi_game()

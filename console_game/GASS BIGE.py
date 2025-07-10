import random
import time

def generate_bridge(length):
    return [random.choice(["L", "R"]) for _ in range(length)]

def print_instructions():
    print("\n🦑 Welcome to Squid Game: Glass Bridge!")
    print("You must cross a bridge by choosing Left (L) or Right (R) at each step.")
    print("One side is tempered glass (safe), the other is regular glass (breaks).")
    print("Choose wrong and you fall!\n")

def play_game():
    bridge_length = 10
    bridge = generate_bridge(bridge_length)
    current_step = 0

    print_instructions()

    while current_step < bridge_length:
        print(f"Step {current_step + 1}/{bridge_length}")
        choice = input("Choose [L]eft or [R]ight: ").strip().upper()

        if choice not in ["L", "R"]:
            print("❌ Invalid input. Please choose 'L' or 'R'.")
            continue

        if choice == bridge[current_step]:
            print("✅ Safe! Moving forward...\n")
            current_step += 1
        else:
            print("💥 CRASH! You picked the wrong glass. You fell!")
            print("Game Over.")
            return

        time.sleep(0.5)

    print("🎉 Congratulations! You crossed the bridge safely!")

if __name__ == "__main__":
    play_game()

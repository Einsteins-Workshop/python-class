import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_top(power, name):
    spin = "🔄" * (power // 2)
    print(f"{name}'s Top Spin Power [{power}]: {spin}")

def spinning_top_game():
    clear()
    print("=== 🌀 Spinning Top – Squid Game Style ===\n")
    print("Spin your top by pressing 's' at the perfect time!")
    print("The faster your reaction, the higher your spin power.\n")
    input("Press Enter to begin...")

    # Get player spin
    print("\nWait for it...")
    time.sleep(random.uniform(2.0, 4.0))
    print("NOW! Press 's' to spin!")
    start_time = time.time()
    key = input(">> ").strip().lower()
    reaction = time.time() - start_time

    if key != 's':
        print("❌ Wrong key! You dropped the top.")
        player_power = 0
    elif reaction > 1.0:
        print(f"⌛ Too slow! ({reaction:.2f}s)")
        player_power = random.randint(1, 4)
    else:
        base_power = max(1, int((1.0 - reaction) * 10))
        player_power = base_power + random.randint(0, 3)
        print(f"🔥 Nice timing! Your reaction: {reaction:.2f}s")

    time.sleep(1)
    print("\n🌀 Your Spin Result:")
    draw_top(player_power, "You")

    # AI Spin
    ai_reaction = random.uniform(0.3, 1.2)
    ai_power = max(1, int((1.0 - ai_reaction) * 10)) + random.randint(0, 3)

    time.sleep(1)
    print("\n🤖 Opponent's Turn...")
    time.sleep(1)
    draw_top(ai_power, "Opponent")

    # Determine Winner
    print("\n🏁 Result:")
    if player_power > ai_power:
        print("🎉 YOU WIN the Spinning Top challenge!")
    elif player_power < ai_power:
        print("😵 You lost. Opponent spun better.")
    else:
        print("🤝 It's a tie! Try again.")

if __name__ == "__main__":
    spinning_top_game()

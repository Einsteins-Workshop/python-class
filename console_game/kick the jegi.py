import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII visuals
def jegi_ascii():
    return r"""
     🥢
    /|\
     |
    / \
    """

def kick_animation():
    return r"""
     🥢
    \|/
     |
    / \
   KICK!
    """

def kick_the_jegi_game():
    clear()
    print("=== 🥢 Kick the Jegi – Squid Game Style ===\n")
    print("Press 'k' to kick the jegi at the right time!")
    print("Each correct kick adds 1 point. Miss a kick and the game ends.\n")
    input("Press Enter to begin...")

    score = 0

    while True:
        clear()
        print(f"Score: {score}")
        print(jegi_ascii())
        print("Wait for the signal...")

        time.sleep(random.uniform(2.0, 4.0))

        print("\nNOW! Press 'k' to kick!")
        start_time = time.time()
        key = input(">> ").strip().lower()
        reaction = time.time() - start_time

        if key != 'k':
            print("❌ Wrong key! The jegi fell.")
            break
        elif reaction > 1.0:
            print(f"⌛ Too slow! ({reaction:.2f}s)")
            break
        else:
            print(kick_animation())
            print("✅ Great kick!")
            score += 1
            time.sleep(1)

    print("\n🏁 Game Over!")
    print(f"🎯 Final Score: {score}")
    if score >= 5:
        print("🎉 You're a Jegi kicking master!")
    elif score >= 3:
        print("👏 Not bad! You passed.")
    else:
        print("😅 Better luck next time!")

if __name__ == "__main__":
    kick_the_jegi_game()

import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_arena(stone_pos):
    arena = ['-'] * 21
    center = 10
    if 0 <= stone_pos <= 20:
        arena[stone_pos] = '🪨'
    arena[center] = '🎯' if stone_pos != center else '💥'  # Hit center
    print("Target: 🎯".center(30))
    print("".join(arena))
    print("         ^ center")

def flying_stone_game():
    clear()
    print("=== 🪨 Flying Stone: Squid Game Style ===\n")
    print("Try to land your stone as close to the 🎯 as possible.")
    print("Press 't' to throw at the right moment (timing matters!)\n")
    input("Press Enter to start...\n")

    best_throw = None
    closest_distance = 21

    for round_num in range(1, 4):
        clear()
        print(f"--- Round {round_num} ---")
        print("Get ready to throw... Wait for the signal.")
        wait = random.uniform(2, 4)
        time.sleep(wait)

        print("\nNOW! Press 't' to throw the stone!")
        start_time = time.time()
        key = input(">> ").strip().lower()
        reaction = time.time() - start_time

        if key != 't':
            print("❌ Wrong key! You dropped the stone.")
            throw_pos = random.randint(0, 20)
        else:
            timing_factor = max(0, 1.5 - reaction)  # Faster = better
            variance = random.randint(-3, 3)
            throw_strength = int((timing_factor * 10)) + variance
            throw_pos = min(20, max(0, throw_strength))

        distance = abs(throw_pos - 10)  # distance from center
        print("\nThrow result:")
        print_arena(throw_pos)
        print(f"Distance from center: {distance}")

        if distance < closest_distance:
            closest_distance = distance
            best_throw = throw_pos

        time.sleep(2)

    clear()
    print("🏁 Game Over! Your best throw:")
    print_arena(best_throw)
    if closest_distance == 0:
        print("🎯 PERFECT HIT! You win the Flying Stone challenge!")
    elif closest_distance <= 2:
        print("👏 Very close! You win!")
    else:
        print("😓 Not close enough. Better luck next time!")

if __name__ == "__main__":
    flying_stone_game()

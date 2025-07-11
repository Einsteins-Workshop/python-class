import time
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# ---------------------------
# Game 1: Dakji
def game_dakji():
    clear()
    print("=== 🎴 DAKJI Challenge ===\n")
    print("Press 's' as fast as you can when 'NOW!' appears to flip the opponent’s tile.")
    input("Press Enter to start...")

    chances = 3
    for attempt in range(1, chances + 1):
        clear()
        print(f"Attempt {attempt} of {chances}")
        print("Get ready...")
        time.sleep(random.uniform(1.5, 3.5))

        print("\nNOW! Slam your tile! (Press 's')")
        start = time.time()
        key = input().strip().lower()
        reaction = time.time() - start

        if key != 's':
            print("❌ Wrong key! Missed your chance.")
        elif reaction > 1.0:
            print(f"⌛ Too slow! ({reaction:.2f}s)")
        else:
            if random.randint(1, 3) == 1:
                print("\n💥 SLAM! You flipped the tile!")
                print("🎉 You WIN the Dakji challenge!")
                time.sleep(2)
                return 1
            else:
                print("\n💢 You hit it but not hard enough. Try again.")
        time.sleep(2)
    print("\n💀 You failed to flip the tile.")
    time.sleep(2)
    return 0


# ---------------------------
# Game 2: Flying Stone
def print_arena(pos):
    arena = ['-'] * 21
    center = 10
    if 0 <= pos <= 20:
        arena[pos] = '🪨'
    arena[center] = '🎯' if pos != center else '💥'
    print("Target: 🎯".center(30))
    print("".join(arena))
    print("         ^ center")


def game_flying_stone():
    clear()
    print("=== 🪨 Flying Stone ===")
    print("Press 't' quickly when 'NOW!' appears to throw your stone close to the target.")
    input("Press Enter to start...")

    best_dist = 21
    best_pos = None

    for rnd in range(1, 4):
        clear()
        print(f"Round {rnd}/3")
        print("Get ready to throw...")
        time.sleep(random.uniform(2, 4))
        print("\nNOW! Press 't' to throw the stone!")
        start = time.time()
        key = input().strip().lower()
        reaction = time.time() - start

        if key != 't':
            print("❌ Wrong key! You dropped the stone.")
            pos = random.randint(0, 20)
        else:
            timing = max(0, 1.5 - reaction)
            variance = random.randint(-3, 3)
            strength = int(timing * 10) + variance
            pos = max(0, min(20, strength))

        dist = abs(pos - 10)
        print("\nThrow result:")
        print_arena(pos)
        print(f"Distance from center: {dist}")
        if dist < best_dist:
            best_dist = dist
            best_pos = pos
        time.sleep(2)
    clear()
    print("🏁 Game Over! Your best throw:")
    print_arena(best_pos)
    if best_dist == 0:
        print("🎯 PERFECT HIT! You win Flying Stone!")
        time.sleep(2)
        return 1
    elif best_dist <= 2:
        print("👏 Very close! You win Flying Stone!")
        time.sleep(2)
        return 1
    else:
        print("😓 Not close enough. You lose Flying Stone.")
        time.sleep(2)
        return 0


# ---------------------------
# Game 3: Gongi
def print_gongi_hand(held, ground):
    print("\nYour hand: " + "🪨" * held)
    print("Stones on ground: " + "🪨" * ground + "\n")


def game_gongi():
    clear()
    print("=== 🪨 Gongi ===")
    print("Pick up stones (press 'p') and toss them at the right time (press 't').")
    print("Try to catch as many as possible. You have 5 stones.")
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
            start = time.time()
            action = input(">> ").lower()
            reaction = time.time() - start

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
    time.sleep(2)
    return 1 if score >= 3 else 0


# ---------------------------
# Game 4: Spinning Top
def draw_top(power, name):
    spin = "🔄" * (power // 2)
    print(f"{name}'s Spin Power [{power}]: {spin}")


def game_spinning_top():
    clear()
    print("=== 🌀 Spinning Top ===")
    print("Press 's' as fast as possible when 'NOW!' appears to spin your top.")
    input("Press Enter to start...")

    print("Wait for it...")
    time.sleep(random.uniform(2, 4))
    print("NOW! Press 's' to spin!")
    start = time.time()
    key = input(">> ").strip().lower()
    reaction = time.time() - start

    if key != 's':
        print("❌ Wrong key! You dropped the top.")
        player_power = 0
    elif reaction > 1.0:
        print(f"⌛ Too slow! ({reaction:.2f}s)")
        player_power = random.randint(1, 4)
    else:
        base = max(1, int((1.0 - reaction) * 10))
        player_power = base + random.randint(0, 3)
        print(f"🔥 Great timing! Reaction: {reaction:.2f}s")

    time.sleep(1)
    print("\nYour Spin Result:")
    draw_top(player_power, "You")

    ai_reaction = random.uniform(0.3, 1.2)
    ai_power = max(1, int((1.0 - ai_reaction) * 10)) + random.randint(0, 3)

    time.sleep(1)
    print("\nOpponent's Turn...")
    time.sleep(1)
    draw_top(ai_power, "Opponent")

    print("\nResult:")
    time.sleep(1)
    if player_power > ai_power:
        print("🎉 You WIN Spinning Top!")
        time.sleep(2)
        return 1
    elif player_power < ai_power:
        print("😵 You LOST Spinning Top.")
        time.sleep(2)
        return 0
    else:
        print("🤝 It's a tie!")
        time.sleep(2)
        return 0


# ---------------------------
# Game 5: Kick the Jegi
def jegi_ascii():
    return r"""
     🥢
    /|\
     |
    / \
    """


def kick_anim():
    return r"""
     🥢
    \|/
     |
    / \
   KICK!
    """


def game_kick_jegi():
    clear()
    print("=== 🥢 Kick the Jegi ===")
    print("Press 'k' quickly when 'NOW!' appears to kick the jegi.")
    input("Press Enter to start...")

    score = 0
    while True:
        clear()
        print(f"Score: {score}")
        print(jegi_ascii())
        print("Wait for the signal...")

        time.sleep(random.uniform(2, 4))

        print("\nNOW! Press 'k' to kick!")
        start = time.time()
        key = input(">> ").strip().lower()
        reaction = time.time() - start

        if key != 'k':
            print("❌ Wrong key! Jegi fell.")
            break
        elif reaction > 1.0:
            print(f"⌛ Too slow! ({reaction:.2f}s)")
            break
        else:
            print(kick_anim())
            print("✅ Great kick!")
            score += 1
            time.sleep(1)

    clear()
    print("Game Over!")
    print(f"Final Score: {score}")
    time.sleep(2)
    return 1 if score >= 3 else 0


# ---------------------------
# Pentathlon main
def pentathlon():
    clear()
    print("=== 🦑 Squid Game Season 2 Pentathlon ===\n")
    input("Press Enter to begin all 5 games!\n")

    total_score = 0
    total_score += game_dakji()
    total_score += game_flying_stone()
    total_score += game_gongi()
    total_score += game_spinning_top()
    total_score += game_kick_jegi()

    clear()
    print("🏁 Pentathlon Complete!")
    print(f"Your total score: {total_score} / 5\n")

    if total_score == 5:
        print("🔥 Incredible! You are the ultimate Squid Game champion!")
    elif total_score >= 3:
        print("👍 Good job! You passed the Pentathlon.")
    else:
        print("😢 Better luck next time. Keep practicing!")


if __name__ == "__main__":
    pentathlon()

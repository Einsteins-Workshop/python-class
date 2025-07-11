import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

player_pos = 0
goal = 10
stamina = 5

def seeker_face(seeking):
    return r"""
    (•_•)   Seeker is watching! 👀
    """ if seeking else r"""
    (•‿•)   Seeker is distracted 😌
    """

def draw_scene(pos, stamina, seeker_alert):
    track = ['-'] * goal
    if pos < goal:
        track[pos] = '🧍'
    else:
        track[-1] = '🏁'
    print("HIDE & SEEK".center(30, '='))
    print(seeker_face(seeker_alert))
    print("Track: " + "".join(track))
    print(f"Stamina: {'💓' * stamina}\n")

def hide_and_seek_game():
    global player_pos, stamina
    print("=== Squid Game: Hide and Seek ===")
    input("Press Enter to begin...")

    while player_pos < goal:
        seeker_alert = random.choice([True, False])
        clear()
        draw_scene(player_pos, stamina, seeker_alert)

        action = input("Action? [w = walk, h = hide]: ").strip().lower()

        if seeker_alert:
            if action == 'h':
                print("🫣 You hid successfully!")
            else:
                print("👁️ Seeker saw you! You've been caught!")
                print("💀 GAME OVER")
                return
        else:
            if action == 'w':
                player_pos += 1
                stamina = min(5, stamina + 1)  # Recover some stamina
                print("🚶 You moved forward.")
            elif action == 'h':
                stamina -= 1
                print("😰 You hid unnecessarily... -1 stamina.")
            else:
                print("❓ Invalid input. You stayed still.")

        if stamina <= 0:
            print("💤 You ran out of stamina from hiding too much!")
            print("💀 GAME OVER")
            return

        time.sleep(1)

    print("\n🎉 You reached the safe zone! YOU WIN!")

if __name__ == "__main__":
    hide_and_seek_game()

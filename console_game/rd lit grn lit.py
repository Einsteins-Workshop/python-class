import random
import time
import sys

# ASCII Art for Doll
doll = r"""
       (o_o)
      /|   |\
      / \ / \
   Red Light Green Light
"""

print("=== Squid Game: Red Light, Green Light ===")
print(doll)
input("Press Enter to start...")

# Game Configuration
goal_distance = 20  # Distance to reach the finish line
player_pos = 0

def print_track(player_pos, goal_distance):
    track = ['-'] * goal_distance
    if player_pos < goal_distance:
        track[player_pos] = '🏃'
    else:
        track[-1] = '🏁'
    print("".join(track))

def red_light_green_light():
    global player_pos
    while player_pos < goal_distance:
        light = random.choice(["green", "red"])
        print()
        print_track(player_pos, goal_distance)
        print(f"\nThe doll is turning...")

        time.sleep(1)
        print(f"🔦 Light: {light.upper()}")

        if light == "green":
            move = input("➡️ Move forward? (press 'm'): ").strip().lower()
            if move == 'm':
                player_pos += 1
                print("✅ You moved forward.")
            else:
                print("⏸️ You stayed still.")
        else:  # red light
            print("⛔ Don't move!")
            time.sleep(1)
            move = input("Did you move? (press 'm' if you moved): ").strip().lower()
            if move == 'm':
                print("\n💥 You were caught moving on RED LIGHT!")
                print("☠️ Game Over.")
                sys.exit()
            else:
                print("😌 You stayed still. Good.")

        time.sleep(1)

    print("\n🏁 You reached the finish line!")
    print("🎉 You Win!")

if __name__ == "__main__":
    red_light_green_light()

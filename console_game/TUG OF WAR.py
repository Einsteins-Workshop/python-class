import time
import random
import os

# Clear screen function (for Windows & Unix)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display ASCII rope and players
def draw_rope(position):
    left = "🧍 Team A"
    right = "Team B 🧍"
    rope = ['-'] * 21  # Middle index is 10
    if 0 <= position <= 20:
        rope[position] = '🪢'
    print(f"\n{left}")
    print("".join(rope))
    print(f"{right}\n")

# Game Logic
def tug_of_war():
    position = 10  # Start in the middle
    win_left = 0
    win_right = 20
    game_speed = 0.5  # Speed of AI pull

    print("=== Squid Game: Tug of War ===")
    print("Tap 'p' rapidly to pull the rope to your side!")
    print("If the rope goes all the way to your side, you win.")
    print("If it goes to the AI's side, you lose.")
    input("Press Enter to begin...")

    clear()
    while True:
        draw_rope(position)

        # Player input with timeout
        start = time.time()
        print("Press 'p' to pull! (You have 1 second)")
        moved = False
        while time.time() - start < 1:
            try:
                import msvcrt  # for Windows
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode().lower()
                    if key == 'p':
                        position -= 1
                        moved = True
                        break
            except ImportError:
                # For Unix-like systems
                import sys
                import select
                import tty
                import termios
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(sys.stdin.fileno())
                    [i, _, _] = select.select([sys.stdin], [], [], 1)
                    if i:
                        key = sys.stdin.read(1)
                        if key.lower() == 'p':
                            position -= 1
                            moved = True
                            break
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        if not moved:
            # AI pulls the rope if you don’t
            position += random.choice([1, 2])
            print("💪 AI pulled the rope!")

        # Clamp position
        position = max(0, min(20, position))
        time.sleep(game_speed)
        clear()

        # Check win/loss
        if position == win_left:
            draw_rope(position)
            print("🎉 You pulled the rope to your side. You WIN!")
            break
        elif position == win_right:
            draw_rope(position)
            print("💀 You were pulled off the platform. You LOSE.")
            break

if __name__ == "__main__":
    tug_of_war()

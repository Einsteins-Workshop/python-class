import os
import time
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

explosion_frames = [
    """
       .
    """,
    """
       .
     . * .
    """,
    """
     . * .
    *  💥  *
     . * .
    """,
    """
     * 💥 * 💥 *
   💥 💥 💥 💥 💥
     * 💥 * 💥 *
    """,
    """
  💥💥💥💥💥💥💥💥💥
 💥🔥🔥🔥🔥🔥🔥🔥💥
 💥🔥💣🔥💣🔥💣🔥💥
 💥🔥🔥🔥🔥🔥🔥🔥💥
  💥💥💥💥💥💥💥💥💥
    """,
    """
    (charred remains...)
       ☠️ ☠️ ☠️
    """
]

def explosion_simulator():
    clear()
    print("=== 💥 EXPLOSION SIMULATOR ===")
    input("Press Enter to ignite the fuse...")

    print("\nIgniting fuse", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    time.sleep(1)

    for frame in explosion_frames:
        clear()
        print(frame)
        time.sleep(0.6)

    print("\n💀 BOOM! That escalated quickly.")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    explosion_simulator()

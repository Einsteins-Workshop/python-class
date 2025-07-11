import random
import time

# ASCII art for shapes
shapes = {
    "circle": """
     _____
    /     \\
   |       |
    \\_____/
    """,
    "triangle": """
       /\\
      /  \\
     /____\\
    """,
    "square": """
    _______
   |       |
   |       |
   |_______|
    """,
    "umbrella": """
       __/\\__
     /       \\
    |         |
     \\_______/
        ||
    """
}


def show_shape(shape_name):
    print(f"\nYour shape is: {shape_name.capitalize()}")
    print(shapes[shape_name])


def scrape_challenge(shape):
    print("\nStart scraping carefully! You must press 's' to scrape.")
    print("Don't press anything else or you'll crack the candy!")

    max_scrapes = 10
    cracks_allowed = 2
    cracks = 0
    scrapes = 0

    while scrapes < max_scrapes:
        action = input(
            f"[Scrapes: {scrapes}/{max_scrapes}, Cracks: {cracks}/{cracks_allowed}] Press 's' to scrape: ").strip().lower()

        if action != 's':
            cracks += 1
            print("⚠️ You cracked the candy!")
            if cracks >= cracks_allowed:
                print("💥 The candy is broken! Game Over.")
                return False
        else:
            scrapes += 1
            print("🪚 Scraping...")

        time.sleep(0.3)

    print("🎉 Success! You carved out the shape without breaking it!")
    return True


def dalgona_game():
    print("=== Dalgona Candy Game ===")
    input("Press Enter to start the game...")

    shape = random.choice(list(shapes.keys()))
    show_shape(shape)
    result = scrape_challenge(shape)

    if result:
        print("🏆 You passed the Dalgona challenge!")
    else:
        print("☠️ You failed the challenge.")


if __name__ == "__main__":
    dalgona_game()

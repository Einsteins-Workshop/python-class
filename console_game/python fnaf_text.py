import time
import random

# ============================
# ASCII Jumpscares
# ============================
def ascii_jumpscare(name):
    art = {
        "Bonnie": r"""
        (\_/)
        ( •_•)   BONNIE GOT YOU!
        />💀
        """,
        "Chica": r"""
        (•ө•) 🍕
        <) )╯   CHICA GOT YOU!
        /  \
        """,
        "Foxy": r"""
        🦊 FOXY RAN INTO YOUR ROOM!
        🏃‍♂️ YOU COULDN'T CLOSE THE DOOR IN TIME!
        ☠️ GAME OVER.
        """,
        "Freddy": r"""
        ʕ•ᴥ•ʔ 🎩
        🎵 DUM DUM DUM 🎵
        🧸 FREDDY GOT YOU IN THE DARK!
        """
    }
    print(art.get(name, "💀"))

# ============================
# Game State
# ============================
power = 100
door_closed = False
camera_on = False
animatronics = {
    "Bonnie": 0,
    "Chica": 0,
    "Foxy": 0,
    "Freddy": 0
}
hours = ["12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM"]
foxy_warning = 0
freddy_active = False

# ============================
# Display Functions
# ============================
def display_status(hour):
    print("\n📟 Time:", hour)
    print(f"🔋 Power: {power}%")
    print("🚪 Door Closed:", "Yes" if door_closed else "No")
    print("📷 Camera On:", "Yes" if camera_on else "No")

def show_camera_map():
    print("\n🖥️  CAMERA FEED")
    rooms = ["[0] Show Stage   ",
             "[1] Dining Area ",
             "[2] Back Hall   ",
             "[3] Supply Closet",
             "[4] Hall Corner ",
             "[5] Office Door "]

    room_display = [""] * 6
    for name, pos in animatronics.items():
        symbol = {
            "Bonnie": "B",
            "Chica": "C",
            "Foxy": "F",
            "Freddy": "R"
        }.get(name, "?")
        room_display[pos] += symbol

    for i in range(6):
        icons = room_display[i] if room_display[i] else "--"
        print(f"{rooms[i]}  |  {icons}")

# ============================
# Game Mechanics (Hard Mode, Medium Power Drain)
# ============================
def move_animatronics(current_hour_index):
    global foxy_warning, freddy_active

    # Higher chance to move in hard mode
    for name in ["Bonnie", "Chica"]:
        if random.random() < 0.6:  # 60% chance to move
            animatronics[name] = min(animatronics[name] + 1, 5)

    if not camera_on:
        foxy_warning += 1
        if foxy_warning >= 2:  # Foxy moves faster in hard mode (2 missed cams)
            animatronics["Foxy"] = min(animatronics["Foxy"] + 1, 5)
            foxy_warning = 0
    else:
        foxy_warning = 0

    if current_hour_index >= 2:  # Freddy activates earlier at 2 AM
        freddy_active = True

    if freddy_active and random.random() < 0.3:  # Freddy moves faster
        animatronics["Freddy"] = min(animatronics["Freddy"] + 1, 5)

def check_attack():
    for name in ["Bonnie", "Chica"]:
        if animatronics[name] >= 5:
            if door_closed:
                print(f"{name} tried to attack, but the door saved you!")
                animatronics[name] = 3
            else:
                ascii_jumpscare(name)
                return True

    if animatronics["Foxy"] >= 4:
        print("\n🏃‍♂️ Foxy is charging down the hallway!")
        if door_closed:
            print("🚪 You slammed the door just in time! Foxy retreats.")
            animatronics["Foxy"] = 2
        else:
            ascii_jumpscare("Foxy")
            return True

    if animatronics["Freddy"] >= 5:
        if not door_closed:
            print("\n🎵 You hear Freddy's music box getting louder...")
            ascii_jumpscare("Freddy")
            return True
        else:
            print("🎩 Freddy giggles outside. The door holds... for now.")
            animatronics["Freddy"] = 4

    return False

def reduce_power():
    global power, door_closed, camera_on
    usage = 2  # base drain (medium speed)
    if camera_on:
        usage += 2  # more drain for camera in hard mode
    if door_closed:
        usage += 4  # more drain for door in hard mode
    power -= usage
    if power < 0:
        power = 0
    if power == 0:
        print("⚡ Power outage! Everything shuts down...")
        door_closed = False
        camera_on = False
        return True
    return False

# ============================
# Main Game Loop
# ============================
def main():
    global power, door_closed, camera_on, animatronics

    print("🎮 Welcome to Five Nights at Freddy's (HARD MODE with MEDIUM POWER DRAIN)")
    input("Press ENTER to begin Night 1...")

    for hour_index in range(6):  # 12 AM to 6 AM
        current_hour = hours[hour_index]
        for _ in range(3):  # fewer decisions per hour (hard mode)
            display_status(current_hour)
            action = input("\nWhat do you do? (camera / door / wait): ").strip().lower()

            if action == "camera":
                camera_on = True
                print("📷 You check the cameras...")
                show_camera_map()
            else:
                camera_on = False

            if action == "door":
                door_closed = not door_closed
                print("🚪 Door is now", "closed." if door_closed else "open.")

            move_animatronics(hour_index)
            reduce_power()

            if check_attack():
                print("💀 You were defeated.")
                return

            time.sleep(0.7)  # faster loop in hard mode

    print("\n🔔 6 AM! You survived the night! 🏆")

# ============================
# Run the Game
# ============================
if __name__ == "__main__":
    main()

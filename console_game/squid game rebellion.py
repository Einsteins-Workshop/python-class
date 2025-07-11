import time
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_rebellion_intro():
    clear()
    print(r"""
   ____            _       _       
  / ___| ___ _ __ | |_ ___| |__    
 | |  _ / _ \ '_ \| __/ __| '_ \   
 | |_| |  __/ | | | || (__| | | |  
  \____|\___|_| |_|\__\___|_| |_|  

Welcome to Squid Game Season 2: REBELLION

You lead the players fighting back against the guards!
Survive the rounds and defeat the Guard Commander.

""")


def print_status(player_hp, allies, guard_hp):
    print(f"Your HP: {player_hp}   |  Allies: {allies}  |  Guard Commander HP: {guard_hp}")


def print_actions():
    print("\nChoose your action:")
    print("1. Attack guards ⚔️")
    print("2. Rally allies 🙌")
    print("3. Defend 🛡️")
    print("4. Status 📊")
    print("5. Quit ❌")


def attack_action(player_hp, allies, guard_hp):
    base_attack = random.randint(15, 30) + allies * 2
    print(f"\nYou and your allies attack fiercely dealing {base_attack} damage!")
    guard_hp -= base_attack
    time.sleep(1)
    return player_hp, allies, guard_hp


def rally_action(player_hp, allies, guard_hp):
    gain = random.randint(1, 3)
    allies += gain
    print(f"\nYou rallied the players! Allies increased by {gain}. Total allies: {allies}")
    time.sleep(1)
    return player_hp, allies, guard_hp


def defend_action(player_hp, allies, guard_hp):
    block = random.randint(15, 35)
    print(f"\nYou prepare to defend and can block up to {block} damage next turn.")
    time.sleep(1)
    return player_hp, allies, guard_hp, block


def guard_attack(player_hp, allies, block):
    guard_attack_power = random.randint(20, 40)
    damage = max(guard_attack_power - block, 0)
    print(f"\nGuards attack with {guard_attack_power} damage! You block {block} damage.")
    print(f"You take {damage} damage.")
    player_hp -= damage
    time.sleep(1)
    return player_hp


def rebellion_game():
    print_rebellion_intro()
    input("Press Enter to start the rebellion...")
    player_hp = 150
    allies = 3
    guard_hp = 200
    block = 0

    turn = 1
    while player_hp > 0 and guard_hp > 0:
        clear()
        print(f"=== Turn {turn} ===")
        print_status(player_hp, allies, guard_hp)
        print_actions()
        choice = input("\nEnter action number: ").strip()

        if choice == '1':
            player_hp, allies, guard_hp = attack_action(player_hp, allies, guard_hp)
            block = 0
        elif choice == '2':
            player_hp, allies, guard_hp = rally_action(player_hp, allies, guard_hp)
            block = 0
        elif choice == '3':
            player_hp, allies, guard_hp, block = defend_action(player_hp, allies, guard_hp)
        elif choice == '4':
            print_status(player_hp, allies, guard_hp)
            input("\nPress Enter to continue...")
            continue
        elif choice == '5':
            print("You fled the rebellion... Game Over.")
            return
        else:
            print("Invalid input! Try again.")
            time.sleep(1)
            continue

        # Guards retaliate unless you quit
        if guard_hp > 0:
            player_hp = guard_attack(player_hp, allies, block)

        if player_hp <= 0:
            clear()
            print("💀 You were defeated by the guards...")
            print("Game Over. The rebellion has failed.")
            return

        if guard_hp <= 0:
            clear()
            print("🎉 You defeated the Guard Commander!")
            print("The rebellion is victorious!")
            return

        turn += 1

    if player_hp <= 0:
        print("You died.")
    elif guard_hp <= 0:
        print("You won!")


if __name__ == "__main__":
    rebellion_game()

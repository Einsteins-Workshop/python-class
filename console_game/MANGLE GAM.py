import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

def get_move():
    move = input("Move (w/a/s/d) or 'q' to quit: ").lower()
    while move not in ['w','a','s','d','q']:
        move = input("Invalid input. Move (w/a/s/d) or 'q' to quit: ").lower()
    return move

def mingle_game():
    clear()
    print("=== 🦑 Squid Game: Mingle Game ===")
    print("You are 'P' - move to find the secret Target among NPCs (N).")
    print("You have 15 moves to find the Target.\n")
    input("Press Enter to start...")

    size = 7
    grid = [['.' for _ in range(size)] for _ in range(size)]

    # Place player
    player_pos = [size//2, size//2]
    grid[player_pos[0]][player_pos[1]] = 'P'

    # Place NPCs (10 random positions, no overlap)
    npc_positions = []
    while len(npc_positions) < 10:
        pos = [random.randint(0,size-1), random.randint(0,size-1)]
        if pos != player_pos and pos not in npc_positions:
            npc_positions.append(pos)
            grid[pos[0]][pos[1]] = 'N'

    # Choose target NPC randomly
    target_pos = random.choice(npc_positions)

    moves_left = 15

    while moves_left > 0:
        clear()
        print(f"Moves left: {moves_left}")
        print_grid(grid)

        move = get_move()
        if move == 'q':
            print("You quit the game. Bye!")
            break

        # Calculate new position
        new_pos = player_pos.copy()
        if move == 'w' and player_pos[0] > 0:
            new_pos[0] -= 1
        elif move == 's' and player_pos[0] < size-1:
            new_pos[0] += 1
        elif move == 'a' and player_pos[1] > 0:
            new_pos[1] -= 1
        elif move == 'd' and player_pos[1] < size-1:
            new_pos[1] += 1
        else:
            print("Can't move there!")
            input("Press Enter to continue...")
            continue

        # Move player
        # Clear old position
        grid[player_pos[0]][player_pos[1]] = '.'

        # If new pos is NPC, ask if player wants to guess
        if new_pos in npc_positions:
            clear()
            print_grid(grid)
            print(f"You found an NPC at position {new_pos}!")
            guess = input("Is this the Target? (y/n): ").lower()
            if guess == 'y':
                if new_pos == target_pos:
                    print("\n🎉 You found the Target! You win the Mingle Game!")
                    return
                else:
                    print("\n❌ Wrong! This NPC is NOT the Target.")
                    moves_left -= 2  # penalty for wrong guess
                    input("Press Enter to continue...")
            else:
                print("\nYou chose not to guess.")
                input("Press Enter to continue...")

        # Place player in new position
        grid[new_pos[0]][new_pos[1]] = 'P'
        player_pos = new_pos

        moves_left -= 1

    clear()
    print("⏰ Time's up! You failed to find the Target.")
    print(f"The Target was at position {target_pos}.")
    print("Game Over!")

if __name__ == "__main__":
    mingle_game()

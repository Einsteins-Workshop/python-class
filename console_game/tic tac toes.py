def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")


def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]):
        return True

    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            move = input(f"Player {current_player}, enter your move (row and column: 1 1): ")
            row, col = map(int, move.strip().split())
            row -= 1
            col -= 1
        except:
            print("Invalid input. Please enter row and column numbers like '1 1'.")
            continue

        if not (0 <= row < 3 and 0 <= col < 3):
            print("Move out of bounds. Try again.")
            continue

        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").strip().lower()
        if replay != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

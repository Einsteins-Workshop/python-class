          # Look at sample_4_input_output.py for example statements

# We are going to print a tic-tac-toe board
# First, store the board state in a list

# Extend the board to contain nine squares
board = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

# Print the board three elements at a time.
print(board[0], "|", board[1], "|", board[2])
print("---------")
# Continue printing the rest of the board
print(board[3], "|", board[4], "|", board[5])
# continue printing the rest of your board
print("---------")
print(board[6], "|", board[7], "|", board[8 ])

# Ask the user for a square
player = input("ask user for square.")
# Replace the appropriate part of the board list with an "X"
player_num = int(player)
board[player_num-1] = "x"
# Print the board again with the new X.
print(board[0], "|", board[1], "|", board[2])
print("---------")
print(board[3], "|", board[4], "|", board[5])
print("---------")
print(board[6], "|", board[7], "|", board[8])

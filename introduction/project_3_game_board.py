# Look at sample_4_input_output.py for example statements

# We are going to print a tic-tac-toe board
# First, store the board state in a list

# Extend the board to contain nine squares
board = [0, 1, 2, 3, 4, 5, 6, 7, 8,]

# Print the board three elements at a time.
print(board[0], "|", board[1], "|", board[2])
print("---------")
print(board[3], "|", board[4], "|", board[5])
print("---------")
print(board[6], "|", board[7], "|", board[8])
# Continue printing the rest of the board

# Ask the user for a square
input1= input("Player 1, choose a square to put your X")
input1=int(input1)
board[input1]="X"
print(board[0], "|", board[1], "|", board[2])
print("---------")
print(board[3], "|", board[4], "|", board[5])
print("---------")
print(board[6], "|", board[7], "|", board[8])
input2= input("Player 2, choose a square to put your Y")
input2=int(input2)
board[input2]="Y"
print(board[0], "|", board[1], "|", board[2])
print("---------")
print(board[3], "|", board[4], "|", board[5])
print("---------")
print(board[6], "|", board[7], "|", board[8])
# Replace the appropriate part of the board list with an "X"
input3= input("Player 1, choose a square for your X")
input3=int(input3)
board[input3]="X"

# Print the board again with the new X.
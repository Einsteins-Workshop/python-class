# Look at sample_4_input_output.py for example statements

# We are going to print a tic-tac-toe board
# First, store the board state in a list

# Extend the board to contain nine squares
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Print the board three elements at a time.

print(board[0], "|", board[1], "|", board[2])
print("---------")
# Continue printing the rest of the board
print(board[3], "|", board[4], "|", board[5])
print("---------")

print(board[6], "|", board[7], "|", board[8])
print("---------")


square_1 = input("Type in a number from 1-9: ")
# Ask the user for a square

board[int(square_1)-1]="X"
# Replace the appropriate part of the board list with an "X"

# Print the board again with the new X.
print(board[0], "|", board[1], "|", board[2])
print("---------")
# Continue printing the rest of the board
print(board[3], "|", board[4], "|", board[5])
print("---------")

print(board[6], "|", board[7], "|", board[8])
print("---------")

square_2 = input("Type in a number from 1-9, except any of the numbers that have been chosen so far: ")
# Ask the user for a square

board[int(square_2)-1]="O"

print(board[0], "|", board[1], "|", board[2])
print("---------")
# Continue printing the rest of the board
print(board[3], "|", board[4], "|", board[5])
print("---------")

print(board[6], "|", board[7], "|", board[8])
print("---------")

square_3 = input("Type in a number from 1-9, except any of the numbers that have been chosen before: ")
# Ask the user for a square

board[int(square_3)-1]="X"

print(board[0], "|", board[1], "|", board[2])
print("---------")
# Continue printing the rest of the board
print(board[3], "|", board[4], "|", board[5])
print("---------")

print(board[6], "|", board[7], "|", board[8])
print("---------")

square_4 = input("Type in a number from 1-9, except any of the numbers that have been chosen before: ")
# Ask the user for a square

board[int(square_4)-1]="O"

print(board[0], "|", board[1], "|", board[2])
print("---------")
# Continue printing the rest of the board
print(board[3], "|", board[4], "|", board[5])
print("---------")

print(board[6], "|", board[7], "|", board[8])
print("---------")

square_5 = input("Type in a number from 1-9, except any of the numbers that have been chosen before: ")
# Ask the user for a square

board[int(square_5)-1]="X"

print(board[0], "|", board[1], "|", board[2])
print("---------")
# Continue printing the rest of the board
print(board[3], "|", board[4], "|", board[5])
print("---------")

print(board[6], "|", board[7], "|", board[8])
print("---------")

square_6 = input("Type in a number from 1-9, except any of the numbers that have been chosen before: ")
# Ask the user for a square

board[int(square_6)-1]="O"

print(board[0], "|", board[1], "|", board[2])
print("---------")
# Continue printing the rest of the board
print(board[3], "|", board[4], "|", board[5])
print("---------")

print(board[6], "|", board[7], "|", board[8])
print("---------")

square_7 = input("Type in a number from 1-9, except any of the numbers that have been chosen before: ")
# Ask the user for a square

board[int(square_7)-1]="X"

print(board[0], "|", board[1], "|", board[2])
print("---------")
# Continue printing the rest of the board
print(board[3], "|", board[4], "|", board[5])
print("---------")

print(board[6], "|", board[7], "|", board[8])
print("---------")

square_8 = input("Type in a number from 1-9, except any of the numbers that have been chosen before: ")
# Ask the user for a square

board[int(square_8)-1]="O"

print(board[0], "|", board[1], "|", board[2])
print("---------")
# Continue printing the rest of the board
print(board[3], "|", board[4], "|", board[5])
print("---------")

print(board[6], "|", board[7], "|", board[8])
print("---------")

square_9 = input("Type in a number from 1-9, except any of the numbers that have been chosen before: ")
# Ask the user for a square

board[int(square_9)-1]="X"

print(board[0], "|", board[1], "|", board[2])
print("---------")
# Continue printing the rest of the board
print(board[3], "|", board[4], "|", board[5])
print("---------")

print(board[6], "|", board[7], "|", board[8])
print("---------")
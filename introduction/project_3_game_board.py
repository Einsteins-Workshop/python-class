      # Look at sample_4_input_output.py for example statements
player = "X"
current_board = []
# We are going to print a tic-tac-toe board
# First, store the board state in a list
board=[0,1,2,3,4,5,6,7,8,9]
turn = 0
def print_board(board):


    print(board[1], "|", board[2], "|", board[3])
    print("---------")
    print(board[4], "|", board[5], "|", board[6])
    print("---------")
    print(board[7], "|", board[8], "|", board[9])
def check_win(board2):

    if (board2 [3] == board2 [5]) and (board2 [5] == board2 [7]):
        print("You won.")
    elif (board2 [1] == board2 [5]) and (board2 [5] == board2 [9]):
        print("You won.")
    elif (board2 [1] == board2 [2]) and (board2 [2] == board2 [3]):
        print("You won.")
    elif (board2 [4] == board2 [5]) and (board2 [5] == board2 [6]):
        print("You won.")
    elif (board2 [7] == board2 [8]) and (board2 [8] == board2 [9]):
        print("You won.")
    elif (board2 [1] == board2 [4]) and (board2 [4] == board2 [7]):
        print("You won.")
    elif (board2 [2] == board2 [5]) and (board2 [5] == board2 [8]):
        print("You won.")
    elif (board2 [3] == board2 [6]) and (board2 [6] == board2 [9]):
        print("You won.")

#while True:
   # print_board(current_board)
    #position = input()

print_board(board)
check_win(board)


square = int(input("choose a number to put a number."))
board[square] = "X"

print_board(board)
check_win(board)


square2 = int(input("choose a number to put a number."))
board[square2] = "O"

print_board(board)
check_win(board)

square = int(input("choose a number to put a number."))
board[square] = "X"

print_board(board)
check_win(board)

square2 = int(input("choose a number to put a number."))
board[square2] = "O"

print_board(board)
check_win(board)


square = int(input("choose a number to put a number."))
board[square] = "X"

print_board(board)
check_win(board)

square2 = int(input("choose a number to put a number."))
board[square2] = "O"

print_board(board)


square = int(input("choose a number to put a number."))
board[square] = "X"

print_board(board)
check_win(board)

square2 = int(input("choose a number to put a number."))
board[square2] = "O"

print_board(board)
check_win(board)


square = int(input("choose a number to put a number."))
board[square] = "X"

print_board(board)
check_win(board)

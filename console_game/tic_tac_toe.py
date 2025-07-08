# First, we want to keep track of the current player, the turn, and the board.  I recommend storing the
# board as a list of nine elements, each keeping track of one of the positions in the 3x3 board
player = "X"
current_board = [1, 2, 3, 4, 5, 6, 7, 8, 9] # TODO: This should be initialized with nine values represent the symbol to choose that square.
turn = 0

# Define a function that prints the board
def print_board(board):
    # This should print the nine board positions with the current value in the board.

    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

# Continue printing the rest of the board

# TODO: Exit loop if there is a winner or all positions have been filled in (on turn nine).
while True:
    # Print the current board state.
    print_board(current_board)

    # TODO: Ask the current player to choose a square.  Make sure that it is an allowable position.# #  ##
    square = int(input("What square do you chose?"))
    print(current_board)
    if square in current_board:
        print("square is availble to be selected")
        current_board[square - 1] = player
        if (current_board[0]==current_board[1]) and(current_board[0]==current_board[2]):  
             print(player + " " + "won")
        elif (current_board[4] == current_board[5]) and (current_board[4] == current_board[6]):
            print(player + " " + "won")
        elif (current_board[7] == current_board[8]) and (current_board[7] == current_board[9]):
            print(player + " " + "won")
        elif (current_board[0] == current_board[4]) and (current_board[0] == current_board[7]):
            print(player + " " + "won")
        if player=="X":
            player="O"
        else:
            player="X"
    else:
        print("That square is chosen")

    # TODO: Check to see if there are is a winner by checking all eight possible three in a row options. If
    # there is a three in a row, declare that player the winner and make sure to exit the loop.


    # TODO: If turn 9 is passed, declare the game a draw and exit the loop.
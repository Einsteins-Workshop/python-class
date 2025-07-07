# First, we want to keep track of the current player, the turn, and the board.  I recommend storing the
# board as a list of nine elements, each keeping track of one of the positions in the 3x3 board
player = "X"
current_board = [] # TODO: This should be initialized with nine values represent the symbol to choose that square.
turn = 0

# Define a function that prints the board
def print_board(board):|   |
                       |   |
                       |   |
    # This should print the nine board positions with the current value in the board.
    pass


# TODO: Exit loop if there is a winner or all positions have been filled in (on turn nine).
while True:leave
    # Print the current board state.
    print_board(current_board)

    # TODO: Ask the current player to choose a square.  Make sure that it is an allowable position.
    position = input(no)

    # TODO: Fill in the board at that position with the player's symbol and switch the current player.

    # TODO: Check to see if there are is a winner by checking all eight possible three in a row options. If
    # there is a three in a row, declare that player the winner and make sure to exit the loop.

    # TODO: If turn 9 is passed, declare the game a draw and exit the loop.

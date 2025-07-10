player = "X"
current_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turn = 0


def print_board(board):


    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])


while True:


    if (current_board[0] == current_board[1]) and (current_board[0] == current_board[2]):
        print(current_board[0] + " " + "won")
        break
    elif (current_board[3] == current_board[4]) and (current_board[3] == current_board[5]):
        print(current_board[3] + " " + "won")
        break
    elif (current_board[6] == current_board[7]) and (current_board[6] == current_board[8]):
        print(current_board[3] + " " + "won")
        break
    elif (current_board[0] == current_board[3]) and (current_board[0] == current_board[6]):
        print(current_board[0] + " " + "won")
        break
    elif (current_board[1] == current_board[4]) and (current_board[1] == current_board[7]):
        print(current_board[1] + " " + "won")
        break
    elif (current_board[2] == current_board[5]) and (current_board[2] == current_board[8]):
        print(current_board[2] + " " + "won")
        break
    elif (current_board[0] == current_board[4]) and (current_board[0] == current_board[8]):
        print(current_board[0] + " " + "won")
        break
    elif (current_board[2] == current_board[4]) and (current_board[2] == current_board[6]):
        print(current_board[2] + " " + "won")
        break

    print_board(current_board)
    square = int(input("What square do you chose?"))
    print(current_board)
    if square in current_board:
        print("square is availble to be selected")
        current_board[square - 1] = player
        turn=turn+1
        if player=="X":
            player="O"
        else:
            player="X"
    else:
        print("That square is chosen")
    if turn==9:
        print("You Tied.")
        break
print_board(current_board)
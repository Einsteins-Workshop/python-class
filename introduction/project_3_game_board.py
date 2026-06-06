# Look at sample_4_input_output.py for example statements

# We are going to print a tic-tac-toe board
# First, store the board state in a list

# Extend the board to contain nine squares
board = [0, 1, 2, 3, 4, 5, 6, 7, 8,]
def print_board(myboard):
    print(myboard[0], "|", myboard[1], "|",  myboard[2])
    print("---------")
    print( myboard[3], "|",  myboard[4], "|",  myboard[5])
    print("---------")
    print( myboard[6], "|",  myboard[7], "|",  myboard[8])

def check_winner(myboard):
    winner = None
    if (myboard[0] == myboard[1]) and (myboard[0] == myboard[2]):
        winner = myboard[0]
    elif (myboard[3] == myboard[4]) and (myboard[4] == myboard[5]):
        winner = myboard[3]
    elif (myboard[6] == myboard[7]) and (myboard[7] == myboard[8]):
        winner = myboard[6]
    elif (myboard[0] == myboard[3]) and (myboard[3] == myboard[6]):
        winner = myboard[0]
    elif (myboard[1] == myboard[4]) and (myboard[4] == myboard[7]):
        winner = myboard[1]
    elif (myboard[2] == myboard[5]) and (myboard[5] == myboard[8]):
        winner = myboard[2]
    elif (myboard[0] == myboard[4]) and (myboard[4] == myboard[8]):
        winner = myboard[0]
    elif (myboard[2] == myboard[4]) and (myboard[4] == myboard[6]):
        winner = myboard [2]
    if winner:
        print(f"We have a winner {winner}!")
        play_new_game()
def play_game():
    # Extend the board to contain nine squares
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, ]
    # Print the board three elements at a time.
    print_board (board)
    print("Do not pick the same box as your opponent.")
    print("First to get 3 X's or Y's in a row wins!")
    print("Can be diagonal or across")
    # Continue printing the rest of the board

    # Ask the user for a square
    input1= input("Player 1, choose a square to put your X")
    input1=int(input1)
    board[input1]="X"
    print_board (board)
    input2= input("Player 2, choose a square to put your Y")
    input2=int(input2)
    while input2 in [input1]:
        print("Player has already chosen this. Choose a different square.")
        print_board(board)
        input2 = input("Player 2, choose a square to put your Y")
        input2 = int(input2)

    board[input2]="Y"
    print_board (board)

    # Replace the appropriate part of the board list with an "X"
    input3= input("Player 1, choose a square for your X")
    input3=int(input3)
    while input3 in [input1, input2]:
        print("Player has already chosen this. Choose a different square.")
        print_board(board)
        input3 = input("Player 1, choose a square for your X")
        input3 = int(input3)
    board[input3]="X"
    print_board (board)
    input4= input("Player 2, choose a square to put your Y")
    input4=int(input4)
    while input4 in [input1, input2, input3]:
        print("Player has already chosen this. Choose a different square.")
        print_board(board)
        input4 = input("Player 2, choose a square to put your Y")
        input4 = int(input4)
    board[input4]="Y"
    print_board (board)
    input5= input("Player 1, choose a square to put your X")
    input5=int(input5)
    while input5 in [input1, input2, input3, input4]:
        print("Player has already chosen this. Choose a different square.")
        print_board(board)
        input5 = input("Player 1, choose a square to put your X")
        input5 = int(input5)
    board[input5]="X"
    print_board (board)
    check_winner(board)

    input6= input("Player 2, choose a square to put your Y")
    input6=int(input6)
    board[input6]="Y"
    while input6 in [input1, input2, input3, input4, input5]:
        print("Player has already chosen this. Choose a different square.")
        print_board(board)
        input6 = input("Player 1, choose a square to put your X")
        input6 = int(input6)

    print_board (board)
    check_winner(board)
    input7= input("Player 1, choose a square to put your X")
    input7=int(input7)
    while input7 in [input1, input2, input3, input4, input5, input6]:
        print("Player has already chosen this. Choose a different square.")
        print_board(board)
        input7 = input("Player 2, choose a square to put your Y")
        input7 = int(input7)
    board[input7]="X"
    print_board (board)
    check_winner(board)
    input8= input("Player 2, choose a square to put your Y")
    input8=int(input8)
    while input8 in [input1, input2, input3, input4, input5, input6, input7]:
        print("Player has already chosen this. Choose a different square.")
        print_board(board)
        input8 = input("Player 1, choose a square to put your X")
        input8 = int(input8)
    board[input8]="Y"
    print_board (board)
    check_winner(board)
    input9= input("Player 1, choose a square to put your X")
    input9=int(input9)
    while input9 in [input1, input2, input3, input4, input5, input6, input7, input8]:
        print("Player has already chosen this. Choose a different square.")
        print_board(board)
        input9 = input("Player 2, choose a square to put your Y")
        input9 = int(input9)
    board[input9]="Y"
    print_board (board)
    check_winner(board)
    print("GAME OVER!")
    check_winner(board)
    print("Tie game!")
    play_new_game()
def play_new_game():
    input10 = input("Play again? Yes or No?")
    if input10 == "yes":
        play_game()
    if input10 == "no":
        exit()

play_game()
age=int(input("Who won?? 1 or 2?\n"))
if age == 1:
    print("Player 1 with the home run! Player 2, sucks to be you")
else:
    print("Player 2 has pulled through! Player 1, looks like you've been outdone")
# Print the board again with the new X.

# if board[inputx) == 'X' or board(inputx)=='Y':
#    print("Bad input")
#    exit()
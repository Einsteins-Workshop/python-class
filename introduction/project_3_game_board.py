my_list = [1,4,6,8]
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(board[0], "|", board[1], "|", board[2])
print(board[3], "|", board[4], "|", board[5])
print(board[6], "|", board[7], "|", board[8])
user = int(input("Choose a square!\n"))
if user == 1:
    print("X", "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    user = int(input("Choose a square!\n"))
if user == 2:
    print(board[0], "|", "X", "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    user = int(input("Choose a square!\n"))
if user == 3:
    print(board[0], "|", board[1], "|", "X")
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])  
    user = int(input("Choose a square!\n"))
if user == 4:
    print(board[0], "|", board[1], "|", board[2])
    print("X", "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    user = int(input("Choose a square!\n"))
if user == 5:
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", "X", "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    user = int(input("Choose a square!\n"))
if user == 6:
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", "X")
    print(board[6], "|", board[7], "|", board[8])
    user = int(input("Choose a square!\n"))
if user == 7:
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print("X", "|", board[7], "|", board[8])
    user = int(input("Choose a square!\n"))
if user == 8:
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", "X", "|", board[8])
    user = int(input("Choose a square!\n"))
if user == 9:
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", "X")
    user = int(input("Choose a square!\n"))
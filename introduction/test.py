with open("Despicible_Me.txt", "r") as f:
    for i in range(40047): # replace 0 with the number of chars in your file
        try:
            f.read(1)
        except UnicodeDecodeError:
            print(i)
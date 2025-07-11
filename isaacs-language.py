from time import sleep

filename = input("Run an isaac's language program: ") + ".isaac.txt"
print()
with open(filename, "r") as f:
    data = f.read()

ignore = False
u = ""
for i in data:
    if ignore:
        print(i, end="")
        ignore = False
    else:
        if i == "\\":
            ignore = True
        elif i == ".":
            sleep(0.05)
        elif i == "> ":
            u = input("\033[34m>\033[0m")
        elif i == "<":
            print(u, end="")
        elif i == ":":
            sleep(1.0)
        elif i == ";":
            sleep(0.25)
        elif i == "?":
            u = input()
        elif i == "!":
            print("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM"
                  "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            sleep(0.05)
            raise Exception(f"{filename} tried to explode your computer.")
        else:
            print(i, end="")

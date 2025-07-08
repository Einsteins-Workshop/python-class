from time import sleep

def output(txt: str):
    for i in [*txt]:
        print(i, end="")
        sleep(0.05)
    print()

# try not to edit these two lines unless you seriously know what you're doing
with open("Despicible_Me.txt", "r") as f:
    Despicible_Me = ""
    for _ in range(99434):
        try:
            Despicible_Me += f.read(1)
        except UnicodeDecodeError:
            Despicible_Me += "`"

output("How old are you")
age = input ()
output (f"oh your {age}")
output ("you might know this")
output (f"{Despicible_Me}")

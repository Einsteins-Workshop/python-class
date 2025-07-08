from time import sleep

def output(txt: str):
    for i in [*txt]:
        print(i, end="")
        sleep(0.05)
    print()

# try not to edit these two lines unless you seriously know what you're doing
with open("bee-movie-script.txt", "r") as f:
    bee_movie_script = f.read()

output("How old are you")
age = input ()
output (f"oh your {age}")
output ("you might know this")
output (f"{bee_movie_script}")



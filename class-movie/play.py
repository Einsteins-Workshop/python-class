from time import sleep
from playsound import playsound

with open("minecraft-movie.txt", "r") as f:
    data = f.read()
for i in data.split("\n"):
    if i == "":
        print()
    else:
        print(i)
        sleep(len(i) * 0.05)
   
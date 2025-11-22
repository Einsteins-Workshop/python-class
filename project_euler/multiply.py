string = (" ")

size = 1000000000000

for i in range(size,-1,-10000000):
    print(i)
    try:
        new_string = string * i
        print(new_string)
    except MemoryError:
        print("Didn't work")

from PIL import Image

import time

# Get current time in seconds since the epoch
seconds = time.time()
print(f"Seconds since epoch: {seconds}") #

# Delay the program for 2 seconds
print("Printed immediately.")
time.sleep(2)
print("Printed after 2 seconds.")
from PIL import Image

import webbrowser

import numpy

Mariokart8_Character_want = input("Type stuff to find Mario things or enter number 1-44 for a mariokart 8 character:")

if Mariokart8_Character_want == ("Random"):
                num = numpy.random.randint(43)
                num=+1

if Mariokart8_Character_want.isnumeric():

        # Then print your mad lib using the user input
        print("Your Character is")

        if int(Mariokart8_Character_want) < 1:
                image_path = "il_fullxfull.4590808898_df8r.webp"

image = Image.open(image_path)
        image.show()
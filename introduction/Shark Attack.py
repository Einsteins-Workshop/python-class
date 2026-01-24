import turtle

import time

# Wait 60 seconds till sharks apper tha

# Commands for controlling window for turtle
turtle_window = turtle.Screen()
turtle_window.bgcolor("light green")
turtle_window.title("Meme")

show_colors = False
def  colors():
    global show_colors
    show_colors = not(show_colors)
    while show_colors:
        turtle.Screen().bgcolor("red")

        time.sleep(0.1)

        turtle.Screen().bgcolor("orange")

        time.sleep(0.1)

        turtle.Screen().bgcolor("yellow")

        time.sleep(0.1)

        turtle.Screen().bgcolor("green")

        time.sleep(0.1)

        turtle.Screen().bgcolor("blue")

        time.sleep(0.1)

        turtle.Screen().bgcolor("purple")

        time.sleep(0.1)


cursor = turtle.Turtle()
cursor.speed(0)
def move_right():
    cursor.forward(50)

# Middle stuff for cursor

turtle.listen()
turtle.onkey(move_right, "d")

def move_left():
    cursor.forward(-50)

turtle.onkey(move_left, "a")

def move_up():
    cursor.left(90)
    cursor.forward(50)
    cursor.right(90)



turtle.onkey(move_up, "w")


def move_down():
    cursor.left(-90)
    cursor.backward(50)
    cursor.right(-90)

def move_Ldiagonal():
    cursor.left(45)
    cursor.backward(-50)
    cursor.right(45)

def move_Rdiagonal():
    cursor.left(145)
    cursor.backward(-50)
    cursor.right(145)

def move_downRdiagonal():
    cursor.left(-145)
    cursor.backward(-50)
    cursor.right(-145)

def move_downLdiagonal():
    cursor.left(-45)
    cursor.backward(-50)
    cursor.right(-45)

cursor.color("orange")

turtle.onkey(move_down, "s")

turtle.onkey(move_Ldiagonal, "e")

turtle.onkey(move_Rdiagonal, "q")

turtle.onkey(move_downRdiagonal, "z")

turtle.onkey(move_downLdiagonal, "x")

turtle.onkey(colors, " ")

turtle.done()


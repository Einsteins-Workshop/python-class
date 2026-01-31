import turtle
import time

t = turtle.Turtle()
turtle.setup(450,500)
t.speed(100)
turtle.bgcolor("lightblue")

# function to cover a square
def square():
    t.begin_fill()
    for x in range (0,4):
        t.fd(30)
        t.left(90)
    t.end_fill()
    t.fd(30)

#functions to paint a few squares
def two():
    for x in range(0,2):
        square()

def three():
    for x in range(0,3):
        square()

def four():
    for x in range(0,4):
        square()

#function for turning back
def rotation():
    t.left(90)
    t.fd(60)
    t.left(90)
# 0
t.hideturtle()
t.up()
t.goto(-180,-240)
# level 1, boots
t.color("brown")
four()
t.fd(120)
four()
rotation()
t.fd(30)

# level 2
three()
t.fd(120)
three()

# level 3, pants
t.rt(180)
t.fd(30)
t.color("blue")
three()
t.fd(60)
three()
t.fd(60)
rotation()

# level 4
t.color("orange")
two()
t.color("blue")
three()
two()
three()
t.color("orange")
two()
t.rt(180)

# level 5
three()
t.color("blue")
three()
three()
t.color("orange")
three()
rotation()

# level 6
two()
t.color("green")
square()
t.color("blue")
square()
t.color("yellow")
square()
t.color("blue")
two()
t.color("yellow")
square()
t.color("blue")
square()
t.color("green")
square()
t.color("orange")
two()
t.rt(180)

# level 7, shirt
t.color("green")
four()
t.color("blue")
four()
t.color("green")
four()
rotation()

# level 8
t.fd(30)
three()
t.color('blue')
square()
t.color("green")
two()
t.color("blue")
square()
t.color("green")
three()
t.rt(180)
t.fd(30)

# level 9
two()
t.color("blue")
square()
t.color("green")
two()
t.color("blue")
square()
t.color("green")
two()
rotation()
t.fd(30)

# level 10, head
t.color('orange')
three()
three()
t.fd(30)
t.rt(180)

# level 11
t.color("brown")
square()
t.color("orange")
four()
t.color("black")
four()
t.fd(30)
rotation()

# level 12
t.color("orange")
three()
t.color("black")
square()
t.color("orange")
three()
t.color("brown")
two()
t.color("orange")
square()
t.color("brown")
square()
t.rt(180)

# level 13
square()
t.color("orange")
square()
t.color("brown")
square()
t.color("orange")
three()
t.color("black")
square()
t.color("orange")
three()
rotation()

# level 14
t.fd(60)
square()
t.color("black")
square()
t.color("orange")
two()
t.color("brown")
three()
t.rt(180)

# level 15
t.color("green")
four()
four()
square()
rotation()

# level 16
t.fd(90)
three()
two()

time.sleep(1)

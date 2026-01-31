import turtle
# See https://www.geeksforgeeks.org/python/turtle-programming-python/ for more information


# Commands for controlling window for turtle
turtle_window = turtle.Screen()
turtle_window.bgcolor("light green")
turtle_window.title("Michaelangelo")

cursor = turtle.Turtle()

# Commands for controlling turtle parameters
cursor.speed(100)

# Turtle movement
cursor.forward(10)
cursor.right(90)
cursor.backward(10)
cursor.left(90)
cursor.forward(20)

cursor.penup()
cursor.forward(10)
cursor.pendown()
cursor.forward(30)

# Pen color for turtle
cursor.color("red")
cursor.forward(30)

=======
cursor.goto(10,10)
cursor.stamp()
cursor.setx(20)
cursor.sety(20)
cursor.dot(10)

# To retain window, must always finish with turtle.done()
turtle.done()

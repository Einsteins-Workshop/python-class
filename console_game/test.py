import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the drawing speed (optional, 0 is fastest)
t.speed(5)

# Draw a square
for _ in range(4):  # Repeat 4 times for a square
    t.forward(100)  # Move forward 100 units
    t.left(90)      # Turn left 90 degrees

# Keep the window open until manually closed
turtle.done()
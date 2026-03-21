
import time
import turtle
from random import randint

ALIGNMENT = "Center"
FONT = ("Arial",20,"normal")
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SCREEN = turtle.Screen()

class Snake:
    def __int__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("triangle")

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = turtle.Turtle("square")
        new_segment.color()("white")

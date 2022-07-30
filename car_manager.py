COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.generate_car()
        self.new_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        self.color(random.choice(COLORS))
        self.goto(340, random.randint(-251, 251))

    def move_car(self):
        self.forward(self.new_speed)

    def speed_update(self):
        self.new_speed = MOVE_INCREMENT + STARTING_MOVE_DISTANCE

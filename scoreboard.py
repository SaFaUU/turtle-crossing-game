FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.write_level()

    def write_level(self):
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", move=False, font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, font=FONT)
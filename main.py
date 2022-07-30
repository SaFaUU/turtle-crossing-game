import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True
screen.listen()
screen.onkey(player.move, key="Up")
cars = CarManager()
score = Scoreboard()
a = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    choice = random.choice(range(0, 7))
    if choice == 6:
        cars = CarManager()
        a.append(cars)
    for item in a:
        item.move_car()
    if player.ycor() > 280:
        player.resetpos()
        score.update_level()
        for new_speed in a:
            new_speed.speed_update()
    for collision_check in a:
        if player.distance(collision_check) < 20:
            game_is_on = False

screen.exitonclick()

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Road Crossing")
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    for car_on_move in cars.all_cars:
        if car_on_move.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() == 280:
        score.increase_score()
        score.update_scoreboard()
        player.goto(0, -280)
        cars.level_up()


screen.exitonclick()
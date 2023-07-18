from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:

            new_turtle = Turtle("square")
            new_turtle.shapesize(stretch_wid=1, stretch_len=2)
            new_turtle.penup()
            new_turtle.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_turtle.goto(300, new_y)
            self.all_cars.append(new_turtle)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT




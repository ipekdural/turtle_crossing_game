import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 6

from turtle import Turtle
from random import randint
import turtle
from time import sleep

turtle.colormode(255)


def rand_color_gen():
    r = random.randint(1, 255)  # Generate a random value between 0 and 1
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        chance=randint(1,6)
        if chance==1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(rand_color_gen())
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_locations = []
            for _ in range(-240, 250, 20):
                y_locations.append(_)
            y = random.choice(y_locations)
            new_car.goto(300, y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed+=MOVE_INCREMENT

    def game_over(self,cars):
        self.speed=STARTING_MOVE_DISTANCE
        for car in self.cars:
            car.reset()
            car.color("white")



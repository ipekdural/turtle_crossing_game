FONT = ("Courier", 16, "normal")
from turtle import Turtle
from time import sleep

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-220,250)
        self.level=1
        self.update_level()
    def update_level(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level:{self.level}",align="center",font=FONT)
    def level_up(self):
        self.level+=1
    def game_over(self):
        self.level=1
        self.goto(0,0)
        self.color("purple")
        self.write(f"Game Over \U0001F622", align="center", font=("Courier",30,"bold"))
        self.goto(-5,-30)
        self.write(f"Press 'r' to restart.", align="center", font=("Courier", 15, "bold"))




import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score_board = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")
def game():
    score_board.clear()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        score_board.update_level()

        car.create_car()

        car.move()
        if player.is_finish_line():
            time.sleep(0.3)
            player.go_to_start()
            score_board.level_up()
            car.level_up()
        for _car in car.cars:
            if _car.distance(player) < 20:
                time.sleep(0.2)
                score_board.clear()
                score_board.game_over()
                player.go_to_start()
                score_board.game_over()
                car.game_over(car.cars)
                game_is_on = False
        screen.update()
    screen.onkey(game,"r")
game()
screen.exitonclick()

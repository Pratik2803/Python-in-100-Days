import time
from turtle import Screen
from player import Player
from car import Car
from scorecard import ScoreCard

counter = 0
car_list = []
is_game_on = True

screen = Screen()
screen.title("The turtle crossing capestone")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
player = Player()
score = ScoreCard()

screen.listen()
screen.onkeypress(player.move, 'Up')

while is_game_on:
    screen.update()

    if counter % 6 == 0:
        car = Car()
        car_list.append(car)

    for car_item in car_list:
        if car_item.distance(player) < 20:
            is_game_on = False
            score.game_over()
        else:
            car_item.move()
            time.sleep(.1)

        if player.ycor() > 270:
            score.inc_score()
            car_item.inc_speed()
            player.goto(0, -280)

    counter = counter + 1

screen.exitonclick()

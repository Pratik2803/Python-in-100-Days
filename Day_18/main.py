from turtle import Turtle, Screen
from data import color_list
import random

timmy = Turtle()
timmy.speed('fastest')
screen = Screen()
screen.colormode(255)
timmy.hideturtle()


x_cor = 0
y_cor = 0
for _ in range(10):
    for _ in range(10):
        timmy.pendown()
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)

    y_cor = y_cor + 30
    timmy.setx(0)
    timmy.sety(y_cor)




screen.exitonclick()

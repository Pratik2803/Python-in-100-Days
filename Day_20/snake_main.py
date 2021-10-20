from turtle import Turtle, Screen
import time
import snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = snake.Snake()
screen.listen()
screen.onkeypress(fun=snake.left, key='Left')
screen.onkeypress(fun=snake.right, key='Right')
screen.onkeypress(fun=snake.down, key='Down')
screen.onkeypress(fun=snake.up, key='Up')


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()




screen.exitonclick()

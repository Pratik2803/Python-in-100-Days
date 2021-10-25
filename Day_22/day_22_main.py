from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.title("!!!! PING PONG !!!!")
screen.bgcolor('black')
screen.tracer(0)
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
score = ScoreBoard()
ball = Ball()
screen.update()
screen.tracer(1)
screen.listen()

screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')

screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

is_game_on = True

while is_game_on:
    ball.move()

    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50) and abs(ball.xcor()) > 360:
        ball.bounce_x()
        ball.inc_speed()

    if ball.xcor() > 390:
        ball.reset_ball()
        screen.tracer(0)
        score.l_point()
        screen.update()
        screen.tracer(1)

    if ball.xcor() < -390:
        ball.reset_ball()
        screen.tracer(0)
        score.r_point()
        screen.update()
        screen.tracer(1)


screen.exitonclick()

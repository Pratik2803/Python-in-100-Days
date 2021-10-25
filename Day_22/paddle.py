from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1
PADDLE_BOUNDARY = 260


class Paddle(Turtle):

    def __init__(self, paddle_position):
        super().__init__()
        self.shape('square')
        self.speed('fastest')
        self.turtlesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.penup()
        self.goto(paddle_position)
        self.color('white')

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < PADDLE_BOUNDARY:
            self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if abs(new_y) < PADDLE_BOUNDARY:
            self.sety(new_y)

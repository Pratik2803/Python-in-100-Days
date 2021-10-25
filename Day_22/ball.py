from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_inc = 1
        self.y_inc = 1
        self.shape('circle')
        self.color('white')
        self.penup()

    def move(self):
        x_cor = self.xcor() + self.x_inc
        y_cor = self.ycor() + self.y_inc
        self.goto(x=x_cor, y=y_cor)

    def bounce_y(self):
        self.y_inc = self.y_inc * -1

    def bounce_x(self):
        self.x_inc = self.x_inc * -1

    def reset_ball(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.bounce_x()
        self.reset_speed()

    def inc_speed(self):
        self.x_inc *= 2
        self.y_inc *= 2

    def reset_speed(self):

        if self.x_inc > 0:
            self.x_inc = 1
            self.y_inc = 1
        else:
            self.x_inc = -1
            self.y_inc = 1

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.color('blue')
        self.shape('circle')
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.penup()
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)



import random
from turtle import Turtle

COLOR = ['red', 'green', 'yellow', 'orange', 'white']
POS_X = 280



class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.speed = 5
        self.create_car()

    def create_car(self):
        self.penup()
        self.shape("square")
        self.color(random.choice(COLOR))
        self.setx(POS_X)
        self.sety(random.randint(-250, 250))
        self.shapesize(stretch_len=2, stretch_wid=1)

    def move(self):
        self.backward(self.speed)

    def inc_speed(self):
        self.speed = self.speed + 5

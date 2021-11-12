from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y =280
SHAPE = 'turtle'
COLOR = 'grey'


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):

        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
        else:
            self.goto(STARTING_POSITION)


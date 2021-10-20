from turtle import Turtle

POSITION = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.setx(POSITION[_])
            self.segments.append(segment)

    def move(self):
        for _ in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[_ - 1].xcor()
            new_y = self.segments[_ - 1].ycor()
            self.segments[_].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

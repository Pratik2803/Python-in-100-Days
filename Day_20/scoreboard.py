from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 8, "normal")
SCOREBOARD_XCOR = 0
SCOREBOARD_YCOR = 285


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.counter = 0
        self.goto(x=SCOREBOARD_XCOR, y=SCOREBOARD_YCOR)
        self.scoreboard_text()

    def scoreboard_text(self):
        self.clear()
        self.write(f"Score: {self.counter}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.counter = self.counter + 1
        self.scoreboard_text()

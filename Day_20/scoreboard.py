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
        self.current_score = 0
        self.high_score = 0
        self.goto(x=SCOREBOARD_XCOR, y=SCOREBOARD_YCOR)

        self.get_highest_score()
        self.scoreboard_text()

    def get_highest_score(self):
        with open(file='./highest_score.txt', mode='r', encoding='utf-8') as f:
            self.high_score = int(f.read())

    def scoreboard_text(self):
        self.clear()
        self.write(f"Score: {self.current_score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def scoreboard_reset(self):
        if self.high_score < self.current_score:
            with open(file='./highest_score.txt', mode='w', encoding='utf-8') as f:
                f.write(str(self.current_score))

        self.scoreboard_text()

    def update_scoreboard(self):
        self.current_score = self.current_score + 1
        self.scoreboard_text()

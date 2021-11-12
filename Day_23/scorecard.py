from turtle import Turtle

SCORE_COLOR = 'white'


class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.scoreboard_setup()

    def scoreboard_setup(self):
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.color(SCORE_COLOR)
        self.write_text()

    def write_text(self):
        text = f"Score: {self.score}"
        self.write(arg=text, move=False, align='left', font=('Arial', 10, 'bold'))

    def inc_score(self):
        self.clear()
        self.score = self.score + 1
        self.write_text()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        text = f"Game over Your score is: {self.score}"
        self.write(arg=text, move=False, align='center', font=('Arial', 10, 'bold'))


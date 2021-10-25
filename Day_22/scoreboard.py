from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.lscore = 0
        self.rscore = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(arg=self.lscore, align='center', font=('Arial', 30, 'bold'))

        self.goto(100, 250)
        self.write(arg=self.rscore, align='center', font=('Arial', 30, 'bold'))

    def r_point(self):
        self.rscore += 1
        self.update_score()

    def l_point(self):
        self.lscore += 1
        self.update_score()

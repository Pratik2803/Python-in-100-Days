from turtle import Turtle


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, x_axies, y_axies, state_name):
        self.goto(x=x_axies, y=y_axies)
        self.write(state_name)

    def game_over(self, states_guessed):
        self.goto(0, 0)
        self.write(f'You guessed {states_guessed} states correct')

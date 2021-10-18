from turtle import Turtle, Screen
import random

colors = ['red', 'green', 'yellow', 'pink', 'grey']
y_axies = [-180, -120, -40, 40, 120]
all_turtles = []
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle color", prompt="Your turtle color is: ")

if user_bet:
    is_race_on = True

for turtle_index in range(5):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_axies[turtle_index])
    all_turtles.append(new_turtle)

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won:  {winning_color} is the winner")
            else:
                print(f"You lost, color {winning_color} is the winner")

        random_fwd = random.randint(0, 10)
        turtle.forward(random_fwd)

screen.exitonclick()

from turtle import Screen
import time
import snake
import food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = snake.Snake()
fud = food.Food()
score = scoreboard.Scoreboard()
screen.listen()
screen.onkeypress(fun=snake.left, key='Left')
screen.onkeypress(fun=snake.right, key='Right')
screen.onkeypress(fun=snake.down, key='Down')
screen.onkeypress(fun=snake.up, key='Up')

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(fud) < 15:
        fud.refresh()
        snake.extend_segment()
        score.update_scoreboard()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 285 or abs(snake.head.ycor()) > 285:
        is_game_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 15:
            is_game_on = False
            score.game_over()

screen.exitonclick()

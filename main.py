from turtle import Screen
import time

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)   # turns off the animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()    # listens for events
# listening for keystrokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

# to move the snake
while game_is_on:
    screen.update()   # updates the turtle screen, only to be used with the tracer off
    time.sleep(0.1)   # to suspend the execution for 0.1 secs
    snake.move()

#   detect collision w/food
    if snake.head.distance(food) < 15:
        food.reposition()
        snake.extend()
        scoreboard.update_score()

#   detect collision w/wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

#   detect collision w/tail
    for part in snake.full_snake[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

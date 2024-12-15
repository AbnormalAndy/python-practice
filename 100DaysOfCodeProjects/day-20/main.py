from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')


# TURN BACK ON
screen.tracer(0)


snake = Snake()


game_is_off = False


while game_is_off != True:
    screen.update()
    time.sleep(0.1)


    snake.move()


    if snake.segments[0].xcor() > 270 or snake.segments[0].xcor() < -270:
        game_is_off = True


    if snake.segments[0].ycor() > 270 or snake.segments[0].ycor() < -270:
        game_is_off = True



screen.exitonclick()


# TO-DO:
# Move snake.
# - Up, down, left, right.

# Create Snake Food
# Detect Collision with Food
# Create Scoreboard
# Detect Collision with Wall
# Detect Collision with Tail

# Snake Class
# Food Class
# Scoreboard Class

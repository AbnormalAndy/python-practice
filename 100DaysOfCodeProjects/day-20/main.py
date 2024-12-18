from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')


screen.tracer(0)


snake = Snake()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_off = False


# Game loop.
while game_is_off != True:
    screen.update()
    time.sleep(0.1)


    snake.move()


    # If snake runs into a wall, game loop ends.
    if snake.segments[0].xcor() > 270 or snake.segments[0].xcor() < -270:
        game_is_off = True


    # If snake runs into a wall, game loop ends.
    if snake.segments[0].ycor() > 270 or snake.segments[0].ycor() < -270:
        game_is_off = True


screen.exitonclick()


# TO-DO:
# Create Snake Food
# Detect Collision with Food
# Create Scoreboard
# Detect Collision with Wall
# Detect Collision with Tail

# Snake Class
# Food Class
# Scoreboard Class

from food import Food
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
import time


# Setup screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')


screen.tracer(0)


# Create snake, food, and scoreboard.
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Listen for keys to move the snake.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Game loop switch.
game_is_off = False


# Game loop.
while game_is_off != True:
    screen.update()
    time.sleep(0.1)


    # Moves snake forward.
    snake.move()

    
    # If snake funs into food, move food.
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()


    # If snake runs into a wall, game loop ends.
    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300:
        game_is_off = True


    # If snake runs into a wall, game loop ends.
    if snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
        game_is_off = True


screen.exitonclick()


# TO-DO:
# Detect Collision with Food
# Create Scoreboard
# Detect Collision with Wall
# Detect Collision with Tail

# Scoreboard Class

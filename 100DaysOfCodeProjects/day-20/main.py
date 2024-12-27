from food import Food
from turtle import Screen
from snake import Snake
import time


# Setup screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')


screen.tracer(0)


# Create snake and food.
snake = Snake()
food = Food()


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


    # If snake runs into a wall, game loop ends.
    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300:
        game_is_off = True


    # If snake runs into a wall, game loop ends.
    if snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
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

import random
from turtle import Turtle, Screen


turtle = Turtle()


# Define turtle to be a fast, small circle.
turtle.shape('circle')
turtle.shapesize(0.75, 0.75, 0)
turtle.speed(0)


# List for degrees to turn.
direction = [90, 180, 270, 360]


# List of colors.
color = [
    'light steel blue',
    'royal blue',
    'sky blue',
    'steel blue',
    'dark cyan',
    'dark slate gray',
    'medium spring green',
    'lime green',
    'gold',
    'dark goldenrod',
    'rosy brown',
    'light pink',
    'medium violet red',
    'dark magenta',
    'medium purple',
    'indigo',
]


# Randomly choices a color and direction then moves forward by 25.
def random_walk():
    turtle.pencolor(random.choice(color))
    turtle.right(random.choice(direction))
    turtle.forward(25)


walk_distance = 0


while walk_distance < 200:
    random_walk()
    walk_distance += 1


screen = Screen()
screen.exitonclick()


# TO-DO
# - Speed of Turtle
# - Random Walk
#     - Random Colors



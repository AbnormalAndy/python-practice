import random
from turtle import Turtle, Screen


tim = Turtle()


tim.shape('circle')
tim.shapesize(0.25, 0.25)


tim.penup()
tim.backward(50)
tim.left(90)
tim.forward(300)
tim.right(90)
tim.pendown()


sides = 3
angle = 360 / sides
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


# Range contributes to angle.
while sides != 25:

    
    tim.color(random.choice(color))


    for i in range(sides):
        tim.forward(100)
        tim.right(angle)


    sides += 1
    angle = 360 / sides


screen = Screen()
screen.exitonclick()


# TO-DO
# - Draw:
#     - Triangle
#     - Square
#     - Pentagon
#     - Hexagon
#     - Heptagon
#     - Octagon
#     - Nonagon
#     - Decagon



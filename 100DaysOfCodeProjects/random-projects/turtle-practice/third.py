import random
import turtle as t




turtle = t.Turtle()
t.colormode(255)


# Define turtle to be a fast, small circle.
turtle.shape('circle')
turtle.shapesize(0.75, 0.75, 0)
turtle.speed(0)


# List for degrees to turn.
direction = [90, 180, 270, 360]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# Randomly choices a color and direction then moves forward by 25.
def random_walk():
    r, g, b = random_color()
    turtle.pencolor(r, g, b)
    turtle.right(random.choice(direction))
    turtle.forward(25)


walk_distance = 0


while walk_distance < 200:
    random_walk()
    walk_distance += 1


screen = t.Screen()
screen.exitonclick()


# TO-DO
# - Speed of Turtle
# - Random Walk
#     - Random Colors



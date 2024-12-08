import random
import turtle as t


turtle = t.Turtle()
t.colormode(255)


# Turle shape, shape size, and speed at which it draws.
turtle.shape('circle')
turtle.shapesize(0.1, 0.1, 0)
turtle.speed(0)


# Create a randome color and returns a tuple.
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# Create spirography with random color and heading set to the direction variable.
def spirography():
    turtle.pencolor(random_color())
    turtle.setheading(direction)
    turtle.circle(100)


direction = 0


while direction < 360:
    spirography()
    direction += 3


screen = t.Screen()
screen.exitonclick()



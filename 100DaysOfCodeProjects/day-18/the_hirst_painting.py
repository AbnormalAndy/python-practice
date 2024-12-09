import color_palette
import random
import turtle as t


turtle = t.Turtle()
t.colormode(255)


turtle.shape('circle')
turtle.ht()
turtle.shapesize(0.1, 0.1, 0)
turtle.speed(0)


def random_color():
    color = random.choice(color_palette.colors)
    return color


def painting(painting_width, painting_height):
    x = (painting_width * 50) / 2
    y = (painting_height * 50) / 2


    # Set the beginning position in the bottom-left corner of the canvas.
    beginning_position = [-x, -y]
    turtle.teleport(beginning_position[0], beginning_position[1])
    

    height = 0


    # Moves the dot to the top by 50 until it reaches the top of the canvas.
    while height < painting_height:


        width = 0


        # Moves the dot to the right by 50 until it reaches the right of the canvas.
        while width < painting_width:
            turtle.dot(10, random_color())
            width += 1
            beginning_position[0] += 50
            turtle.teleport(beginning_position[0], beginning_position[1])



        height += 1
        beginning_position[0] = -x
        beginning_position[1] += 50
        turtle.teleport(beginning_position[0], beginning_position[1])
    

painting(13, 13)


screen = t.Screen()
screen.exitonclick()



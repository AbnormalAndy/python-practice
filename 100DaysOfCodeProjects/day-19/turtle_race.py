import random
import turtle as t


colors = [
        'black',
        'light slate gray',
        'cornflower blue',
        'deep sky blue',
        'cyan',
        'aquamarine',
        'spring green',
        'sea green',
        'dark khaki',
        'pale goldenrod',
        'gold',
        'orange',
        'firebrick',
        'coral',
        'crimson',
        'pale violet red',
        'violet',
        'lavender'
        ]


def random_color():
    color = random.choice(colors)
    return color


turtle_list = []


def turtle_create():
    turtle_color = random_color()
    turtle = {}
    turtle['name'] = turtle_color
    turtle['color'] = turtle_color
    return turtle


turtle_count = 10
position_start = (turtle_count * 50) / 2


for i in range(turtle_count):
    turtle_list.append(turtle_create())


for i in range(len(turtle_list)):
    turtle_list[i]['name'] = t.Turtle()
    turtle_list[i]['name'].shape('turtle')
    turtle_list[i]['name'].color(turtle_list[i]['color'])
    turtle_list[i]['name'].teleport(0, position_start)
    position_start -= 50


print(turtle_list)


# This can be a for loop:
# - Generates a turtle.
# - Chooses a color.
# - Teleports to starting line.
#     - 25, 50, 50 = 125


'''
turtle_purple = t.turtle()
turtle_blue = t.turtle()
turtle_green = t.turtle()
turtle_yellow = t.turtle()
turtle_orange = t.turtle()
turtle_red = t.turtle()
'''


screen = t.Screen()
screen.exitonclick()


# TO-DO
# - Create six turtles.
#    - Each turtle is a different color.
# - Randomize the movement forward for each.
#    - Function for this?
# - Declare a winner by creating an arbitrary line.
#    - Could be if a turtle makes it to such coordinate, wins.
#    - Could be if a turtle travels a certain distance, wins.

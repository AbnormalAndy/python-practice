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


def turtle_create():
    turtle_color = random_color()
    turtle = {}
    turtle['name'] = turtle_color
    turtle['color'] = turtle_color
    return turtle


def user_guess_outcome(turtle_winner_position, user_guess):
    if turtle_winner_position == user_guess:
        return True
    else:
        return False


screen = t.Screen()
user_guess = screen.numinput("Turtle RACE", "Who will win the race? Enter a position (1-10):", minval=1, maxval=10)
user_guess -= 1


finish_line = t.Turtle()
finish_line.ht()
finish_line.pensize(3)
finish_line.teleport(300, 400)
finish_line.right(90)
finish_line.forward(800)


turtle_count = 10


x_position_start = -300
y_position_start = 300
y_position_spacing = 600 / turtle_count


turtle_list = []


for i in range(turtle_count):
    turtle_list.append(turtle_create())


for i in range(len(turtle_list)):
    turtle_list[i]['name'] = t.Turtle()
    turtle_list[i]['name'].shape('turtle')
    turtle_list[i]['name'].color(turtle_list[i]['color'])
    turtle_list[i]['name'].teleport(x_position_start, y_position_start)
    turtle_list[i]['name'].penup()
    y_position_start -= y_position_spacing


end_race = False


while end_race != True:
    for i in range(len(turtle_list)):
        turtle_list[i]['name'].forward(random.randint(0, 100))
        if turtle_list[i]['name'].position()[0] > 300:
            winner = i
            #print(f"The {turtle_list[i]['color']} turtle at the {i + 1} position wins the race!")
            end_race = True
            break


screen.exitonclick()


print(f"The {turtle_list[winner]['color']} turtle at the {winner + 1} position wins the race!")
if user_guess_outcome(winner, user_guess):
    print("You win!")
else:
    print("You lose!")



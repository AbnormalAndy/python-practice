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


# Choices a random color from the colors list.
def random_color():
    color = random.choice(colors)
    return color


# Creates a dictionary with turtle name and color.
def turtle_create():
    turtle_color = random_color()
    turtle = {}
    turtle['name'] = turtle_color
    turtle['color'] = turtle_color
    return turtle


# Evaluates users choice to see if their guess was correct.
def user_guess_outcome(turtle_winner_position, user_guess):
    if turtle_winner_position == user_guess:
        return True
    else:
        return False


# Takes user input on who will win the race based on position.
screen = t.Screen()
user_guess = screen.numinput("Turtle RACE", "Who will win the race? Enter a position (1-10):", minval=1, maxval=10)
user_guess -= 1


# Finish line of the race.
finish_line = t.Turtle()
finish_line.ht()
finish_line.pensize(3)
finish_line.teleport(300, 400)
finish_line.right(90)
finish_line.forward(800)


turtle_count = 10


# Starting position of the race.
x_position_start = -300
y_position_start = 300
y_position_spacing = 600 / turtle_count


turtle_list = []


# Generates a list of dictionaries with turtle name and color that is dependent on turtle count.
for i in range(turtle_count):
    turtle_list.append(turtle_create())


# Creates turtles and teleports them to the designated starting line.
for i in range(len(turtle_list)):
    turtle_list[i]['name'] = t.Turtle()
    turtle_list[i]['name'].shape('turtle')
    turtle_list[i]['name'].color(turtle_list[i]['color'])
    turtle_list[i]['name'].teleport(x_position_start, y_position_start)
    turtle_list[i]['name'].penup()
    y_position_start -= y_position_spacing


end_race = False


# Iterates through turtles, moving each of them forward at a random pace.
while end_race != True:
    for i in range(len(turtle_list)):
        turtle_list[i]['name'].forward(random.randint(0, 100))
        if turtle_list[i]['name'].position()[0] > 300:
            winner = i
            #print(f"The {turtle_list[i]['color']} turtle at the {i + 1} position wins the race!")
            end_race = True
            break


screen.exitonclick()


# Evaluate and print outcome of race.
print(f"The {turtle_list[winner]['color']} turtle at the {winner + 1} position wins the race!")
if user_guess_outcome(winner, user_guess):
    print("You win!")
else:
    print("You lose!")



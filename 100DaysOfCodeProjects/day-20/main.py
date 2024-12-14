from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


segment_list = []


# Starting positions in tuple.
starting_positions = [(0, 0), (-20, 0), (-40, 0)]


# Creates new segments.
for position in starting_positions:
    segment = Turtle()
    segment.shape('square')
    segment.color('white')
    segment.penup()
    segment.goto(position)
    segment_list.append(segment)


screen.update()


end = False


# Segments move together.
while end != True:
    for segment_number in range(len(segment_list) - 1, 0, -1):
        new_x = segment_list[segment_number - 1].xcor()
        new_y = segment_list[segment_number - 1].ycor()
        segment_list[segment_number].goto(new_x, new_y)


    segment_list[0].forward(10)
    segment_list[0].left(90)


    screen.update()


    if segment_list[0].xcor() > 270:
        end = True



# Turtle in for loop.
# If add to loop, add another segment?


screen.exitonclick()


# TO-DO:
# Create snake body.
# - 3 squares.
# - 20x20 = Turtle

# Move snake.
# - Up, down, left, right.

# Create Snake Food
# Detect Collision with Food
# Create Scoreboard
# Detect Collision with Wall
# Detect Collision with Tail

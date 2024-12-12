from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')


segment_count = 3
segment_list = []


position_x = 0
position_y = 0


for i in range(segment_count):
    turtle = Turtle()
    turtle.shape('square')
    turtle.color('white')
    turtle.penup()
    turtle.teleport(position_x, position_y)
    position_x -= 20


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

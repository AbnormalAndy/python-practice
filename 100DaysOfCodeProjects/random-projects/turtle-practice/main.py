from turtle import Turtle, Screen


timmy_the_turtle = Turtle()
timmy_the_turtle.shape('circle')
timmy_the_turtle.shapesize(1, 1, 10)
timmy_the_turtle.color('white')


timmy_the_turtle.pencolor('black')
timmy_the_turtle.forward(180)


timmy_the_turtle.pencolor('white')
timmy_the_turtle.right(90)
timmy_the_turtle.forward(180)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(360)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(360)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(360)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(180)


screen = Screen()
screen.bgcolor('black')
screen.exitonclick()



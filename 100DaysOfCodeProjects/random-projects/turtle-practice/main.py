from turtle import Turtle, Screen


tim = Turtle()
tim.shape('circle')
tim.shapesize(1, 1, 10)
tim.color('white')


tim.pencolor('white')
tim.penup()
tim.forward(180)
tim.left(90)
tim.forward(180)
tim.right(180)
tim.pendown()


# TO-DO
# Make a SQUARE class?


for i in range(4):
    tim.forward(360)
    tim.right(90)


tim.left(90)


for i in range(10):
    tim.penup()
    tim.forward(5)
    tim.pendown()
    tim.forward(5)


tim.penup()
tim.right(90)
tim.forward(180)


screen = Screen()
screen.bgcolor('black')
screen.exitonclick()



import turtle as t


turtle = t.Turtle()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def move_left():
    turtle.left(5)


def move_right():
    turtle.right(5)


screen = t.Screen()


screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.listen()


screen.exitonclick()



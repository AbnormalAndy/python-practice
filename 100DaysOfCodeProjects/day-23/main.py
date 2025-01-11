from frog import Frog
from turtle import Screen


WIDTH, HEIGHT = 600, 600


screen = Screen()


screen.title('Turtle Crossing')
screen.bgcolor('black')


screen.tracer(0)


screen.setup(WIDTH + 4, HEIGHT + 8)


frog = Frog()


screen.listen()


screen.onkey(frog.move_up, "Up")
screen.onkey(frog.move_right, "Right")
screen.onkey(frog.move_left, "Left")


game_is_off = False


while game_is_off != True:
    screen.update()


    if frog.ycor() > 270:
        frog.reset()


screen.exitonclick()

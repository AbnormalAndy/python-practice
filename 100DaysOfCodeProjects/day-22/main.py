from paddle import Paddle
from turtle import Screen, Turtle


WIDTH, HEIGHT = 1200, 600


screen = Screen()


screen.title('Pong')
screen.bgcolor('black')


screen.setup(WIDTH + 4, HEIGHT + 8)


paddle = Paddle()


screen.exitonclick()



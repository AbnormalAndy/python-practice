from paddle import Paddle
from turtle import Screen, Turtle
import time


WIDTH, HEIGHT = 1200, 600


screen = Screen()


screen.title('Pong')
screen.bgcolor('black')


screen.tracer(0)


screen.setup(WIDTH + 4, HEIGHT + 8)


paddle = Paddle()


#paddle_player = paddle.create_paddle_player()
#paddle_computer = paddle.create_paddle_computer()


screen.listen()
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")


game_is_off = False


while game_is_off != True:
    screen.update()


screen.exitonclick()



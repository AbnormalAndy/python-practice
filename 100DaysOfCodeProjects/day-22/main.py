from paddle import Paddle
from turtle import Screen, Turtle
import time


WIDTH, HEIGHT = 1200, 600


STARTING_POSITION_PLAYER_EASY = [(550, 40), (550, 20), (550, 0), (550, -20), (550, -40)]
STARTING_POSITION_PLAYER_HARD = [(550, 20), (550, 0), (550, -20)]


STARTING_POSITION_COMPUTER_EASY = [(-550, 20), (-550, 0), (-550, -20)]
STARTING_POSITION_COMPUTER_HARD = [(-550, 40), (-550, 20), (-550, 0), (-550, -20), (-550, -40)]


screen = Screen()


screen.title('Pong')
screen.bgcolor('black')


screen.tracer(0)


screen.setup(WIDTH + 4, HEIGHT + 8)


paddle_player = Paddle(STARTING_POSITION_PLAYER_EASY)
paddle_computer = Paddle(STARTING_POSITION_COMPUTER_EASY)


screen.listen()


screen.onkey(paddle_player.move_up, "Up")
screen.onkey(paddle_player.move_down, "Down")


game_is_off = False


while game_is_off != True:
    screen.update()


screen.exitonclick()



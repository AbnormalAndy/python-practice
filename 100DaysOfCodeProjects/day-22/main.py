from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from turtle import Screen, Turtle
import time


WIDTH, HEIGHT = 1200, 600


# Starting position for player paddle.
STARTING_POSITION_PLAYER_EASY = [(550, 40), (550, 20), (550, 0), (550, -20), (550, -40)]
STARTING_POSITION_PLAYER_HARD = [(550, 20), (550, 0), (550, -20)]


# Starting position for computer paddle.
STARTING_POSITION_COMPUTER_EASY = [(-550, 20), (-550, 0), (-550, -20)]
STARTING_POSITION_COMPUTER_HARD = [(-550, 40), (-550, 20), (-550, 0), (-550, -20), (-550, -40)]


screen = Screen()


screen.title('Pong')
screen.bgcolor('black')


screen.tracer(0)


screen.setup(WIDTH + 4, HEIGHT + 8)


paddle_player = Paddle(STARTING_POSITION_PLAYER_EASY)
paddle_computer = Paddle(STARTING_POSITION_COMPUTER_EASY)


ball = Ball()
heading = 45
ball.setheading(heading)


scoreboard = Scoreboard()

screen.listen()


screen.onkey(paddle_player.move_up, "Up")
screen.onkey(paddle_player.move_down, "Down")


game_is_off = False


while game_is_off != True:
    screen.update()


    ball.move()


    # Y=300, -300; X=600, -600


    # Ball bounces off player paddle.
    for paddle_segment in paddle_player.segments:
        if paddle_segment.distance(ball) < 15:
            heading = heading - 90
            ball.setheading(heading)


    # Ball bounces off computer paddle.
    for paddle_segment in paddle_computer.segments:
        if paddle_segment.distance(ball) < 15:
            heading = heading - 90
            ball.setheading(heading)

    
    # Ball interacts with the bottom of the screen.
    if ball.ycor() < -290:
        heading = heading - 90
        ball.setheading(heading)


    # Ball interacts with the top of the screen.
    if ball.ycor() > 290:
        heading = heading - 90
        ball.setheading(heading)


    # Score for player paddle.
    if ball.xcor() < -600:
        scoreboard.increase_score_player()
        ball.refresh()
        time.sleep(1.5)


    # Score for computer paddle.
    if ball.xcor() > 600:
        scoreboard.increase_score_computer()
        ball.refresh()
        time.sleep(1.5)


    # Player wins.
    if scoreboard.score_player == 2:
        game_is_off = True
        scoreboard.game_over(scoreboard.player)


    # Computer wins.
    if scoreboard.score_computer == 2:
        game_is_off = True
        scoreboard.game_over(scoreboard.computer)


screen.exitonclick()



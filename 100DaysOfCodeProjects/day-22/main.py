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


# Difficulty
EASY = 8
MEDIUM = 6
HARD = 4


screen = Screen()


screen.title('Pong')
screen.bgcolor('black')


screen.tracer(0)


screen.setup(WIDTH + 4, HEIGHT + 8)


paddle_player = Paddle(STARTING_POSITION_PLAYER_EASY)
paddle_computer = Paddle(STARTING_POSITION_COMPUTER_HARD)


ball = Ball()
heading = 45
ball.setheading(heading)


scoreboard = Scoreboard()

screen.listen()


screen.onkey(paddle_player.move_up, "Up")
screen.onkey(paddle_player.move_down, "Down")


game_is_off = False
counter = 0


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


    print(ball.ycor())
    print(paddle_computer.segments[1].ycor())


    # Moves computer paddle. Counter delays computer input to not automatically win.
    if counter == EASY:
        if paddle_computer.segments[1].ycor() >= 0 and paddle_computer.segments[1].ycor() < ball.ycor():
            paddle_computer.move_up()
        if paddle_computer.segments[1].ycor() >= 0 and paddle_computer.segments[1].ycor() > ball.ycor():
            paddle_computer.move_down()
        if paddle_computer.segments[1].ycor() <= 0 and paddle_computer.segments[1].ycor() < ball.ycor():
            paddle_computer.move_up()
        if paddle_computer.segments[1].ycor() <= 0 and paddle_computer.segments[1].ycor() > ball.ycor():
            paddle_computer.move_down()

        counter = 0


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


    counter += 1


screen.exitonclick()


# TO-DO
# - Deflecting ball off paddle is a full 180 when it should be 90?

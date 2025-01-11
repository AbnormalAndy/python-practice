from car import Car
from frog import Frog
from line import Line
from scoreboard import Scoreboard
from turtle import Screen
import random


WIDTH, HEIGHT = 600, 600


XCOR_POSITION_LEFT = 350
YCOR_POSITION_LEFT = [250, 210, 170, 130, 90, 50, -50, -90, -130, -170, -210, -250]


XCOR_POSITION_RIGHT = -350
YCOR_POSITION_RIGHT = [230, 190, 150, 110, 70, 30, -30, -70, -110, -150, -190, -230]


COLOR = ['cornflower blue', 'light sky blue', 'turquoise', 'spring green', 'gold', 'moccasin', 'tomato', 'salmon', 'pink', 'pale violet red']


screen = Screen()


screen.title('Turtle Crossing')
screen.bgcolor('black')


screen.tracer(0)


screen.setup(WIDTH + 4, HEIGHT + 8)


# Cars spawn from right and move left.
car_list_left = []


for i in range(len(YCOR_POSITION_LEFT)):
    car_list_left.append(Car(random.choice(COLOR), XCOR_POSITION_LEFT, YCOR_POSITION_LEFT[i], random.uniform(0.1, 1.0)))


for i in range(1000):
    for car in car_list_left:
        car.move_car_left()


# Cars spawn from left and move right.
car_list_right = []


for i in range(len(YCOR_POSITION_RIGHT)):
    car_list_right.append(Car(random.choice(COLOR), XCOR_POSITION_RIGHT, YCOR_POSITION_RIGHT[i], random.uniform(0.1, 1.0)))


for i in range(1000):
    for car in car_list_right:
        car.move_car_right()


frog = Frog()
line = Line()
scoreboard = Scoreboard()


screen.listen()


screen.onkey(frog.move_up, "Up")
screen.onkey(frog.move_right, "Right")
screen.onkey(frog.move_left, "Left")


game_is_off = False


while game_is_off != True:
    screen.update()


    # Resets frog and increases car speed after completing the level.
    if frog.ycor() > 270:
        scoreboard.increase_level()
        frog.reset()


        for car in car_list_left:
            car.increase_speed()

        for car in car_list_right:
            car.increase_speed()


    # Move cars from right to the left as well as detect collision with frog.
    for car in car_list_left:
        if car.distance(frog) < 20:
            scoreboard.game_over()
            game_is_off = True

        
        if car.distance(frog) < 25 and car.ycor() == frog.ycor():
            scoreboard.game_over()
            game_is_off = True


        if car.xcor() < -320:
            car.reset(XCOR_POSITION_LEFT)
        
        
        car.move_car_left()

        
    # Move cars from left to the right as well as detect collision with frog.
    for car in car_list_right:
        if car.distance(frog) < 20:
            scoreboard.game_over()
            game_is_off = True

        
        if car.distance(frog) < 25 and car.ycor() == frog.ycor():
            scoreboard.game_over()
            game_is_off = True


        if car.xcor() > 320:
            car.reset(XCOR_POSITION_RIGHT)
        
        
        car.move_car_right()


screen.exitonclick()



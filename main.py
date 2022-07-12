import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

tinny=Player()
screen.onkey(tinny.movet,"Up")

car=CarManager()
scoreboard=Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.createcar()
    car.movecar()
    # checking collision with car
    pos=tinny.pos()
    if car.checkcollision(pos) == True:
        scoreboard.gameover()
        game_is_on=False

    #if banda reach the top
    if tinny.ycor()==280:
        print("bete moj kardi")
        tinny.setpos(0, -280)
        car.incspeed()
        scoreboard.updatelevelvalue()
        scoreboard.updatelevel()
screen.exitonclick()
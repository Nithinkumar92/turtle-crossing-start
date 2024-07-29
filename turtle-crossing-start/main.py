import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FONT = ("Courier", 24, "normal")

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
play=Player()
screen.onkey(play.move,"w")

car = CarManager()
score=Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.createcar()
    car.moveleft()
    if play.ycor()>300:
        play.player()
        score.increase()
        score.update()
        car.levelup()
    for c in car.cars:
        if c.distance(play)<20:
           play.up()
           play.goto(0,0)
           play.write("GAME OVER",align="center",font=FONT)
           game_is_on = False






screen.exitonclick()

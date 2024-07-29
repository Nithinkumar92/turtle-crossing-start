COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.cars=[]
        self.carspeed=STARTING_MOVE_DISTANCE



    def createcar(self):
        random_choice=random.randint(1,6)
        if random_choice==2:
            tom=Turtle()
            Y_VALUE = random.randint(-300, 300)
            tom.color(random.choice(COLORS))
            tom.up()
            tom.goto(300, Y_VALUE)
            tom.shape("square")
            tom.shapesize(stretch_wid=1, stretch_len=3)
            tom.setheading(180)
            self.cars.append(tom)



    def moveleft(self):
        for i in self.cars:
            i.penup()
            i.goto(i.xcor()-self.carspeed,i.ycor())

    def levelup(self):
        self.carspeed+=MOVE_INCREMENT








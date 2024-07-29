FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.value=0
        self.update()


    def update(self):
        self.clear()
        self.up()
        self.hideturtle()
        self.goto(-240, 250)
        self.color("black")
        self.write(f"LEVEL:{self.value}", align="center", font=FONT)

    def increase(self):
        self.value+=1
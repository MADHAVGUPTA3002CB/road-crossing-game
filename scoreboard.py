from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.level=1    
        self.updatelevel()
    def updatelevel(self):
        self.clear()
        self.write(f"LEVEL {self.level}",align='center',font=FONT)

    def updatelevelvalue(self):
        self.level+=1

    def gameover(self):
        self.goto(0,0)
        self.write("HAR GYA",align='center',font=FONT)
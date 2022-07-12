COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

import random
from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.carlist=[]
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
    def createcar(self):
        chance=random.randint(1,6)
        if chance==1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(1,2,1)
            randomy=random.randint(-200,200)
            car.penup()
            car.goto(300,randomy)
            self.carlist.append(car)
            

    def movecar(self):
        for car in self.carlist:
            car.backward(self.STARTING_MOVE_DISTANCE)
    
    def checkcollision(self,pos):
        for car in self.carlist:
            if car.distance(pos)<23:
                print("collisoin ho gya")
                return True
    
    def incspeed(self):
        self.STARTING_MOVE_DISTANCE+=10
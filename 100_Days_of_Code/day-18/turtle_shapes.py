from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
num = 3
angle = 0
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"] 
runs = 7


def shapes(num):
    angle = (360 / num) 
    for _ in range(num):
        tim.forward(100)
        tim.right(angle)    


while runs != 0:
    runs -= 1
    shapes(num)
    num += 1
    tim.color(random.choice(colors))








screen = Screen()
screen.exitonclick()
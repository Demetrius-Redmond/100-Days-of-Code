import random
import turtle
from turtle import goto
color_list = [(220, 230, 236), (166, 17, 53), (229, 203, 81), (219, 161, 82), (162, 72, 17), (6, 96, 51), (177, 17, 12), (56, 23, 50), (203, 159, 178), (65, 136, 25), (206, 31, 88), (233, 69, 35), (5, 65, 141), (4, 77, 23), (17, 156, 221), (16, 142, 204), (215, 47, 101)]
turtle.colormode(255)
tim = turtle.Turtle()
tim.pensize(20)
tim.shape("circle")
place = 0
go = -200
tim.penup()
tim.speed("fastest")
tim.hideturtle()
def artwork():
    for x in range(0, 10):
        global place
        tim.color(random.choice(color_list))
        tim.penup() 
        tim.stamp()    
        tim.forward(50) 
        
          
for x in range(0, 10):
    
    go += 50
    tim.goto(-200,go)
    artwork()


screen = turtle.Screen()
screen.exitonclick()
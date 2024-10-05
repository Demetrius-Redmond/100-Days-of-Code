from turtle import Turtle, Screen
import random
import turtle
tim = Turtle()
turtle.colormode(255) 
directions = [1, 2, 3, 4]
rand_color = ""
def random_color(rand_color):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return  rand_color

while True:
    tim.width(20)
    tim.speed(20)
    
    tim.color(random_color(rand_color))
    rand_direction = random.choice(directions)
    if rand_direction == 1:
        tim.forward(50)
    elif rand_direction == 2:    
        tim.back(50)
    elif rand_direction == 3:
        tim.left(50)
    else:
        tim.right(50)
   





screen = Screen()
screen.exitonclick()
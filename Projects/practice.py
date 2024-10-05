from turtle import Turtle, Screen
import random
import turtle
rand_color = ""
t = Turtle()
turtle.colormode(255)

t.speed("fastest")


def random_color(rand_color):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return  rand_color

def spirograph():
    for _ in range(0,36):
        
        t.pencolor(random_color(rand_color))
        t.circle(150, 10)
        t.stamp()

spirograph()

# clockwise




# change shape to circle outline
# random color, print circle, tilt repeat














screen = Screen()
screen.exitonclick()
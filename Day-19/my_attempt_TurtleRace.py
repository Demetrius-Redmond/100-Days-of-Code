from turtle import Turtle, Screen


screen = Screen()
turtle_racer = ""

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def racers(turtle_racer):
    
    turtle_color = ""
    turtle_color += turtle_racer
    turtle_racer = Turtle(shape="turtle")
    turtle_racer.penup()
    turtle_racer.color(turtle_color)
    if turtle_color == "red":
        turtle_racer.goto(x = -240, y = 125)
    elif turtle_color == "orange": 
        turtle_racer.goto(x = -240, y = 75)
    elif turtle_color == "yellow": 
        turtle_racer.goto(x = -240, y = 25)
    elif turtle_color == "green": 
        turtle_racer.goto(x = -240, y = -25)
    elif turtle_color == "blue": 
        turtle_racer.goto(x = -240, y = -75)
    elif turtle_color == "purple": 
        turtle_racer.goto(x = -240, y = -125)


racers("red")
racers("orange")
racers("yellow")
racers("green")
racers("blue")
racers("purple")



screen.exitonclick()
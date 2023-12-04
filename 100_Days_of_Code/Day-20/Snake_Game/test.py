from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor("black")
snake = Turtle("square")
snake.color("white")
snake.penup()

while True:
    snake.forward(5)
def direction():
    up = snake.setheading(90)
    down = snake.setheading(270)
    right = snake.setheading(0)
    left = snake.setheading(180)

    screen.listen()
    screen.onkey(fun= up, key="w" )
    screen.onkey(fun= snake.down, key="s")
    screen.onkey(fun= snake.right,key="a"  )
    screen.onkey(fun= snake.left, key="d")















screen.exitonclick()
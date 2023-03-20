from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()
# screen.onkey(key="space", fun=move_forward)

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()

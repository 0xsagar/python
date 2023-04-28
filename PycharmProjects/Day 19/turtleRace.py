from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a colour: ")
colour = ["red", "orange", "blue", "green", "purple", "yellow"]
y_position = [150, 90, 30, -30, -90, -150]
all_turtle = []
# colour and position of turtle
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(colour[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle has won the race.")
            else:
                print(f"You've lost! The {winning_colour} turtle has won the race.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

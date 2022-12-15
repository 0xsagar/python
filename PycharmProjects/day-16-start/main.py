import turtle
from turtle import Turtle, Screen
import another_module
# print(another_module.another_variable)
#
# timmy = Turtle()
# print(timmy)
#
# timmy.shape("turtle")
# timmy.color("blue4")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# print(table)
# table.align = "l"
# print(table)

# from turtle import Turtle, Screen
# timmy_the_turtle = Turtle()
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for a in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# Three methods to import module
# import turtle
# tim = turtle.Turtle()

# from turtle import Turtle
# tom = Turtle()

# from turtle import *
# tum = Turtle()

# Rename the module name (used when the name of the module is too big)
# import turtle as t
# tim = t.Turtle()

#import heroes
# print(heroes.gen())
from turtle import Turtle, Screen
import random
tim = Turtle()
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# colors=["medium aquamarine", "wheat", "SeaGreen", "LightSeaGreen", "IndianRed", "DeepSkyBlue", "DarkOrchid", "SlateGrey"]
# for _ in range(3,11):
#     tim.color(random.choice(colors))
#     a = 360/_
#     for n in range(_):
#         tim.forward(100)
#         tim.right(a)


# colors=["medium aquamarine", "wheat", "SeaGreen", "LightSeaGreen", "IndianRed", "DeepSkyBlue", "DarkOrchid", "SlateGrey"]
# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(speed="fast")
# for _ in range(69):
#     tim.color(random.choice(colors))
#     tim.forward(40)
#     tim.setheading(random.choice(direction))



# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(speed="fastest")
# turtle.colormode(255)
# def diff_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# for _ in range(100):
#     tim.color(diff_color())
#     tim.forward(40)
#     tim.setheading(random.choice(direction))


# tim.speed(speed="fastest")
# turtle.colormode(255)
# def different_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         tim.color(different_color())
#         tim.circle(100)
#         tim.right(size_of_gap)
# draw_spirograph(5)
screen=turtle.Screen()
screen.exitonclick()
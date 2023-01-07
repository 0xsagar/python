import turtle as turtle_module
import random
tim = turtle_module.Turtle()
turtle_module.colormode(255)
color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
              (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252),
              (243, 33, 165)]

for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
screen = turtle_module.Screen()
screen.exitonclick()

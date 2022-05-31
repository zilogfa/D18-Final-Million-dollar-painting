# Ali Jafarbeglou - A Million Dollar painting ! 10 x 10 dots -  OOP (Turtle/Colorgram)
import random
import turtle
from turtle import Turtle,Screen

# import colorgram
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_list.append(new_color)
# print(rgb_list)

color_list = [
    (227, 172, 8), (247, 156, 94), (218, 197, 209), (252, 198, 98),
    (240, 178, 152), (178, 193, 186), (213, 235, 225),
    (182, 197, 190), (219, 175, 184), (244, 132, 137), (233, 199, 14), (145, 129, 38)
]


dot = Turtle("circle") # changed shape of turtle to circle
turtle.colormode(255) # changing color mode to rgb
dot.hideturtle() # hide turtle
dot.penup()  # hide line
print(random.choice(color_list))

y = -200 # starting point of first dot
for i in range(10): # painting 10 x 10 dots with random color
    dot.goto(-250, y) # starting point of first dot
    for n in range(10):
        dot.color(random.choice(color_list)) # random color from list
        dot.dot(20) # dot size
        dot.forward(50) # movement
    y += 50


screen = Screen()
screen.exitonclick()
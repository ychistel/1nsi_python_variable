from turtle import *

n = 100
r = 150
angle = (180-360/n)

circle(r)
left(90)
for i in range(n):
    forward(r)
    right(angle)
    forward(r)
    left(180)
hideturtle()

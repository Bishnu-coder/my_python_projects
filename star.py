#how to make a star using turtle

from turtle import *

penup()
goto(-100,-20)
pendown()

try:
    for i in range(400):
        speed(0)
        forward(300-(i+3)*2)
        left(120)
        hideturtle()
        if i>300:
            penup()
except Exception as e:
    print("closed")
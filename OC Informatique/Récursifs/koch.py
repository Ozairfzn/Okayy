from turtle import *

speed("fastest")
penup()
goto(-300, -100)
pendown()
angle = 60


def koch(l, n):
    if n == 0:
        forward(l)
    else:
        koch(l/3, n-1)
        left(angle)
        koch(l/3, n-1)
        right(2*angle)
        koch(l/3, n-1)
        left(angle)
        koch(l/3, n-1)


koch(600, 3)
exitonclick()

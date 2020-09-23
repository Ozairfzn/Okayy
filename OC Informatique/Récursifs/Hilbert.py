from turtle import *

speed("fastest")
penup()
goto(-400, 350)
pendown()
l = 40


def hilbert(angle, n):
    if n == 0:
        return
    else:
        left(-angle)
        hilbert(-angle, n-1)
        forward(l)
        left(angle)
        hilbert(angle, n-1)
        forward(l)
        hilbert(angle, n-1)
        left(angle)
        forward(l)
        hilbert(-angle, n-1)
        left(-angle)


hilbert(90, 4)
exitonclick()

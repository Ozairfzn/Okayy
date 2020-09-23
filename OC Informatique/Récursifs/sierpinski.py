from turtle import *

speed("fastest")
penup()
goto(-300, -275)
pendown()


def triange(l, n):
    if n == 0:
        return
    else:
        for i in range(3):
            triange(l/2, n-1)
            forward(l)
            left(120)


triange(600, 6)
exitonclick()

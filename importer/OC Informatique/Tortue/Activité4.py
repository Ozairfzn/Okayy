from turtle import *


penup()
goto(-165, -200)
pendown()
taille = 500
speed("fastest")
width(3)


def tri(taille):
    n = 0
    while n < 2 and taille > 10:
        if n == 0:
            for i in range(3):
                forward(taille)
                left(120)
        else:
            for i in range(3):
                forward(taille)
                left(120)
                tri(taille//2)
        n += 1


print(tri(taille))
exitonclick()

from turtle import *
from math import *

n = 2
modulo = 100
speed("fastest")
delay(0)


L = []
posi = []
for i in range(modulo):
    L.append((i, (n * i) % modulo))
    angle = i * (2*pi/modulo)
    x = 180 * cos(angle)
    y = 180 * sin(angle)
    posi.append((x, y))


for i in range(modulo):
    penup()
    goto(posi[L[i][0]])
    pendown()
    goto(posi[L[i][1]])

exitonclick()

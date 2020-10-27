"""
A : avance d’une quantité fixée (en traçant),
g : tourne à gauche, sans avancer, d’un angle fixé (120°),
d : tourne à droite d’un angle fixé (30°)

"A" ,("A","A[gA]A[dA][A]")
"A" ,("A","A[gA]A[dA]A")
"A" ,("A","AAd[dAgAgA]g[gAdAdA]")

"""

import random
from turtle import *

delay(0)
speed("fastest")
penup()
goto(0, -500)
left(90)
pendown()
color("red")


def iterer_lsysteme(depart, regle, k):
    res = ""
    ini = depart
    for i in range(k):
        for j in ini:
            if j == regle[0]:
                res += regle[1]
            else:
                res += j
        ini, res = res, ""
    return ini


pile = []
for i in (iterer_lsysteme("A", ("A", "A[gA]A[dA][A]"), 5)):
    if i == "A":
        forward(random.randint(20, 30))
    elif i == "g":
        left(random.randint(20, 30))
    elif i == "d":
        right(random.randint(20, 30))
    elif i == "[":
        pile.append((position(), heading()))
    elif i == "]":
        element = pile.pop()
        penup()
        goto(element[0])
        setheading(element[1])
        pendown()


exitonclick()

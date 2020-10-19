"""
A ou B : avance d’une quantité fixée (en traçant),
g : tourne à gauche, sans avancer, d’un angle fixé (120°),
d : tourne à droite d’un angle fixé (-120°)

("A", "AdBgAgBdA"), ("B", "BB")
"""


from turtle import *


speed("fastest")
penup()
goto(-500, -300)
pendown()
color("red")


def iterer_lsysteme_2(depart, regle1, regle2, k):
    res = ""
    ini = depart
    for i in range(k):
        for j in ini:
            if j == regle1[0]:
                res += regle1[1]
            elif j == regle2[0]:
                res += regle2[1]
            else:
                res += j
        ini, res = res, ""
    return ini


for i in (iterer_lsysteme_2("AdBdB", ("A", "AdBgAgBdA"), ("B", "BB"), 5)):
    if i == "A" or i == "B":
        forward(20)
    elif i == "g":
        left(-120)
    elif i == "d":
        right(-120)


exitonclick()

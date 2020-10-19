"""
A ou B : avance d’une quantité fixée (en traçant),
g : tourne à gauche, sans avancer, d’un angle fixé (le plus souvent 90 degrés),
d : tourne à droite d’un angle fixé


flacon de koch: ("A","AgAdAdAgA")
autre règle:
                ("A","AdAgAgAAdAdAgA")
                ("A","AgAAdAAdAdAgAgAAdAdAgAgAAgAAdA")
                ("A","AAdAdAdAdAA")
                ("A","AAdAddAdA")
                ("A","AAdAdAdAdAdAgA")
                ("A","AAdAgAdAdAA")
                ("A","AdAAddAdA")
                ("A","AdAgAdAdA")
"""


from turtle import *


def iterer_lsysteme_1(depart, regle, k):
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


regle = ("A", "AgAdAdAgA")
speed("fastest")
penup()
goto(-500, -300)
pendown()
color("red")


for i in (iterer_lsysteme_1("A", regle, 5)):
    if i == "A" or i == "B":
        forward(5)
    elif i == "g":
        left(90)
    elif i == "d":
        right(90)

exitonclick()

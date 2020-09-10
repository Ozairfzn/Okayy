from turtle import *

speed("fastest")
width(3)

penup()
goto(75, 50)
pendown()

color("blue")
for i in range(5):
    forward(50)
    left(72)


penup()
goto(-150, -150)
pendown()

color("red")
for i in range(5):
    forward(100)
    left(72)


penup()
goto(75, -150)
pendown()

color("purple")
for i in range(8):
    forward(65)
    left(360//8)


penup()
goto(-100, 100)
pendown()

color("green")
longueur = 5
for i in range(20):
    forward(longueur)
    left(45)
    longueur += 3

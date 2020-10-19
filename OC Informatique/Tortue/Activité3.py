from turtle import *
import math


def f(x):
    return 0.01*x**2 - 8


def s(x):
    return math.sin(1/20*x)*100 - 105


X = []
Y = []
for i in range(-200, 200):
    X.append(i)
    Y.append(f(i))


speed(10)
penup()
goto(X[0], Y[0])
pendown()

width(3)
color("blue")
for i in range(399):
    goto(X[i], Y[i])

X_sin = []
Y_sin = []
for i in range(-200, 200):
    X_sin.append(i)
    Y_sin.append(s(i))

penup()
goto(X_sin[0], Y_sin[0])
pendown()

width(3)
color("red")
for i in range(399):
    goto(X_sin[i], Y_sin[i])


exitonclick()

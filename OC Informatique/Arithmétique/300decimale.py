from decimal import *


pr = 324
getcontext().prec = pr


def f(x):
    return x**2 - 2


def bal(a, pas):
    while f(a) < 0:
        a += pas
    while f(a) > 0:
        a -= pas
    return a


def zeros(prec):
    a = 0
    for i in range(1, prec):
        a = bal(Decimal(a), Decimal(10**-i))
    return Decimal(a)


print(zeros(pr))

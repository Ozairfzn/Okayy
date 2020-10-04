from decimal import *


pr = 300
getcontext().prec = pr


def f(x):
    return x**2 - 2


def bal(a, pas):
    if f(a) < 0:
        while f(a) < 0:
            a += pas
    else:
        while f(a) > 0:
            a -= pas
    return a-pas, a


def zeros(prec):
    a = 0
    for i in range(1, prec+1):
        a = bal(Decimal(a), Decimal(10**-i))[0]
    return Decimal(a)


print(zeros(pr-1))

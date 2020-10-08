from decimal import *

pr = 10_000
getcontext().prec = pr


def f(x):
    return x**2 - 2


def df(x):
    return 2*x


g = 1
for i in range(1, pr//50):
    g -= f(Decimal(g))/df(Decimal(g))
print(g)

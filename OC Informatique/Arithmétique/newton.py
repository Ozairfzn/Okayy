from decimal import *


pr = 10_000
getcontext().prec = pr
boucle = int(pr**0.5)


def f(x):
    return x**2 - 2


def df(x):
    return 2*x


g = 1
for i in range(1, boucle):
    g -= f(Decimal(g))/df(Decimal(g))

print(g)

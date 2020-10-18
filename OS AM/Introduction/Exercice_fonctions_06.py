def f(x):
    return x**2 - 3


def bal(a, pas):
    if f(a) < 0:
        while f(a) < 0:
            a += pas
    else:
        while f(a) > 0:
            a -= pas
    return a-pas, a


print(bal(1, 10**-5))

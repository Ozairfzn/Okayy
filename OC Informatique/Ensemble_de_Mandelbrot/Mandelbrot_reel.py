
def f(x, y, a, b): return (x**2 - y**2 + a), (2*x*y + b)


def iterer(a, b):
    maxiter = 100
    x, y = 0, 0
    i = 0

    while x**2 + y**2 <= 4 and i < maxiter:
        x, y = f(x, y, a, b)
        i += 1

    if maxiter == i:
        return 0
    return i

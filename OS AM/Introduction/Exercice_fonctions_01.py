import math


def f(x):
    if x >= 1:
        return x + 1
    else:
        return -(x**2)


def g(x):
    return math.sin(x)


def f_o_g(x):
    return f(g(x))


def g_o_f(x):
    return g(f(x))


def tab(fonction, depart, arrive, pas):
    x = []
    y = []
    while depart <= arrive:
        x.append(depart)
        y.append(fonction(depart))
        depart += pas
        print(f"{depart} --> {fonction(depart)}")


a = 3
d = -1
p = 0.5

print("\nf(x)\n")
tab(f, d, a, p)
print("\ng(x)\n")
tab(g, d, a, p)
print("\nf_o_g(x)\n")
tab(f_o_g, d, a, p)
print("\ng_o_f(x)\n")
tab(g_o_f, d, a, p)

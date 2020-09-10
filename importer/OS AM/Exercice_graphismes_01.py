import math
import matplotlib.pyplot as plt

def f(x):
    return abs(x)

def g(x):
    return math.sin(x)

def h(x):
    return math.sqrt(x)

def j(x):
    return f(x+2)

def k(x):
    return 3*g(2*x)


def tab(fonction, depart, arrive, pas):
    x = []
    y = []
    while depart <= arrive:
        x.append(depart)
        y.append(fonction(depart))
        depart += pas
    return x, y


plt.plot(tab(f, -5, 5, 0.1)[0], tab(f, -5, 5, 0.1)[1], "g-", label = "f")
plt.plot(tab(g, -5, 5, 0.1)[0], tab(g, -5, 5, 0.1)[1], "k--", label = "g")
plt.plot(tab(h, 0, 5, 0.1)[0], tab(h, 0, 5, 0.1)[1], "b-.",label = "h")
plt.plot(tab(j, -5, 5, 0.1)[0], tab(j, -5, 5, 0.1)[1], "r-",label = "j")
plt.plot(tab(k, -5, 5, 0.1)[0], tab(k, -5, 5, 0.1)[1], "m-",label = "k")

plt.axis([-5, 7, -4, 5])
plt.xlabel("x")
plt.ylabel("y")
plt.legend(fontsize=12)
plt.grid(True)
plt.xticks(range(-5, 5, 1), fontsize=12)
plt.yticks(range(-5, 5, 1), fontsize=12)
plt.show()
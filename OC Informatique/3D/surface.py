import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x, y): return x**2 - y**2


xmin, xmax = -1, 1
ymin, ymax = -1, 1
nombres_points = 50


def liste_points_x(x):
    global nombres_points, ymin, ymax
    L = []
    h = (ymax-ymin)/nombres_points
    for k in range(nombres_points+1):
        y = ymin + k*h
        L.append((x, y, f(x, y)))
    return L


def liste_points_y(y):
    global nombres_points, xmin, xmax
    L = []
    h = ((xmax-xmin)/nombres_points)
    for k in range(nombres_points+1):
        x = xmin + k*h
        L.append((x, y, f(x, y)))
    return L


def trace_ligne(liste_points, couleur="gray"):
    liste_x = [x for x, y, z in liste_points]
    liste_y = [y for x, y, z in liste_points]
    liste_z = [z for x, y, z in liste_points]

    ax.plot(liste_x, liste_y, liste_z, color=couleur, linewidth=1)
    return


def trace_surface():
    global nombres_points, xmin, ymin

    h = ((xmax-xmin)/nombres_points)
    for i in range(nombres_points+1):
        x = xmin + i*h
        y = ymin + i*h
        trace_ligne(liste_points_x(x), "blue")
        trace_ligne(liste_points_y(y), "red")
    return


fig = plt.figure()
ax = fig.gca(projection='3d', proj_type='ortho')
trace_surface()
plt.show()

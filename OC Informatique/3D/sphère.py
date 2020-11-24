import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt, sin, cos, asin, pi


def latlong_vers_xyz(r, phi, lam):
    x = r * cos(phi) * cos(lam)
    y = r * cos(phi) * sin(lam)
    z = r * sin(phi)
    return (x, y, z)


def xyz_vers_latlong(x, y, z):
    r = sqrt(x**2 + y**2 + z**2)
    phi = -asin(z/r)
    lam = asin((1/cos(phi))*(y/r))
    return (r, phi, lam)


def trace_meridien(r, lam, nombres_points=100, couleur="red"):
    h = 2*pi/nombres_points

    liste_x = []
    liste_y = []
    liste_z = []
    for k in range(nombres_points+1):
        phi = -pi + h*k
        x, y, z = (latlong_vers_xyz(r, phi, lam))
        liste_x.append(x)
        liste_y.append(y)
        liste_z.append(z)

    ax.plot(liste_x, liste_y, liste_z, color=couleur, linewidth=1)
    return


def trace_parallelles(r, phi, nombres_points=100, couleur="blue"):
    h = 2*pi/nombres_points

    liste_x = []
    liste_y = []
    liste_z = []
    for k in range(nombres_points+1):
        lam = -pi + h*k
        x, y, z = (latlong_vers_xyz(r, phi, lam))
        liste_x.append(x)
        liste_y.append(y)
        liste_z.append(z)

    ax.plot(liste_x, liste_y, liste_z, color=couleur, linewidth=1)
    return


def trace_sphere(r, nombres_points=20):
    h = 2*pi/nombres_points

    for k in range(nombres_points+1):
        lamphi = -pi + h*k
        trace_meridien(r, lamphi)
        trace_parallelles(r, lamphi)


fig = plt.figure()
ax = fig.gca(projection='3d', proj_type='ortho')
trace_sphere(10)
plt.show()

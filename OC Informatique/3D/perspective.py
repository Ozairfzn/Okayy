import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


cube = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1),
        (0, 1, 1), (0, 0, 1), (0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1), (1, 1, 0), (0, 1, 0), (0, 1, 1)]


def afficher_cube_3D(cube, couleur="red"):
    liste_x = [x for x, y, z in cube]
    liste_y = [y for x, y, z in cube]
    liste_z = [z for x, y, z in cube]

    ax.plot(liste_x, liste_y, liste_z, color=couleur, linewidth=1)


fig = plt.figure()
ax = fig.gca(projection='3d', proj_type='ortho')
afficher_cube_3D(cube)
plt.show()

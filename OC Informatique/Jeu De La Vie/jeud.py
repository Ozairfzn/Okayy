from random import *

taille = 5
nouveau_tableau = [[randint(0, 1) for j in range(taille)]
                   for i in range(taille)]


def nombre_voisins(i, j, tab):
    voisins = 0
    # LES 4 COINS
    if i == 0 and j == 0:
        if tab[i][j+1] == 1:
            voisins += 1
        if tab[i+1][j+1] == 1:
            voisins += 1
        if tab[i+1][j] == 1:
            voisins += 1
    elif i == taille-1 and j == taille-1:
        if tab[i][j-1] == 1:
            voisins += 1
        if tab[i-1][j-1] == 1:
            voisins += 1
        if tab[i-1][j] == 1:
            voisins += 1
    elif i == taille-1 and j == 0:
        if tab[i][j+1] == 1:
            voisins += 1
        if tab[i-1][j+1] == 1:
            voisins += 1
        if tab[i-1][j] == 1:
            voisins += 1
    elif i == 0 and j == taille-1:
        if tab[i][j-1] == 1:
            voisins += 1
        if tab[i+1][j-1] == 1:
            voisins += 1
        if tab[i+1][j] == 1:
            voisins += 1
    # LES 4 LINES
    elif i == 0:
        if tab[i][j-1] == 1:
            voisins += 1
        if tab[i][j+1] == 1:
            voisins += 1
        if tab[i+1][j-1] == 1:
            voisins += 1
        if tab[i+1][j] == 1:
            voisins += 1
        if tab[i+1][j+1] == 1:
            voisins += 1
    elif i == taille-1:
        if tab[i][j-1] == 1:
            voisins += 1
        if tab[i][j+1] == 1:
            voisins += 1
        if tab[i-1][j-1] == 1:
            voisins += 1
        if tab[i-1][j] == 1:
            voisins += 1
        if tab[i-1][j+1] == 1:
            voisins += 1
    elif j == 0:
        if tab[i-1][j] == 1:
            voisins += 1
        if tab[i+1][j] == 1:
            voisins += 1
        if tab[i][j+1] == 1:
            voisins += 1
        if tab[i-1][j+1] == 1:
            voisins += 1
        if tab[i+1][j+1] == 1:
            voisins += 1
    elif j == taille-1:
        if tab[i-1][j] == 1:
            voisins += 1
        if tab[i+1][j] == 1:
            voisins += 1
        if tab[i][j-1] == 1:
            voisins += 1
        if tab[i-1][j-1] == 1:
            voisins += 1
        if tab[i+1][j-1] == 1:
            voisins += 1
    # CENTRE
    else:
        if tab[i][j-1] == 1:
            voisins += 1
        if tab[i][j+1] == 1:
            voisins += 1
        if tab[i-1][j-1] == 1:
            voisins += 1
        if tab[i-1][j] == 1:
            voisins += 1
        if tab[i-1][j+1] == 1:
            voisins += 1
        if tab[i+1][j+1] == 1:
            voisins += 1
        if tab[i+1][j-1] == 1:
            voisins += 1
        if tab[i+1][j] == 1:
            voisins += 1
    return voisins


def evolution(tableau):
    tab = [[0 for j in range(taille)]
           for i in range(taille)]
    for i in range(taille):
        for j in range(taille):
            if nombre_voisins(i, j, tableau) == 3:
                tab[i][j] = 1
            elif nombre_voisins(i, j, tableau) == 2 and tableau[i][j] == 1:
                tab[i][j] = 1
            else:
                tab[i][j] = 0
    return tab


for i in range(taille):
    print(nouveau_tableau[i])

print()
nouveau_tableau = evolution(nouveau_tableau)

for i in range(taille):
    print(nouveau_tableau[i])

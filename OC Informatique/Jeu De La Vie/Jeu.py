from tkinter import *
from random import *

hauteur = 800
taille = 20
t = [[0 for j in range(taille)]
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


def tableau(tab):
    echelle = hauteur//taille
    for i in range(taille):
        for j in range(taille):
            if tab[i][j] == 1:
                canvas.create_rectangle(
                    i*echelle, j*echelle, (i+1)*echelle, (j+1)*echelle, fill="red")
            else:
                canvas.create_rectangle(
                    i*echelle, j*echelle, (i+1)*echelle, (j+1)*echelle)


def action_bouton():
    canvas.delete("all")
    global t
    t = evolution(t)
    tableau(t)
    return


def action_clic_souris(event):
    global t
    canvas.delete("all")
    canvas.focus_set()
    x = event.x
    y = event.y
    i = (x*taille)//hauteur
    j = (y*taille)//hauteur
    if t[i][j] == 0:
        t[i][j] = 1
    elif t[i][j] == 1:
        t[i][j] = 0
    tableau(t)
    return


def aleatoire():
    global t
    canvas.delete("all")
    t = [[randint(0, 1) for j in range(taille)]
         for i in range(taille)]
    tableau(t)


root = Tk()
canvas = Canvas(root, width=hauteur, height=hauteur, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

tableau(t)

canvas.bind("<Button-1>", action_clic_souris)
bouton_couleur = Button(root, text="Evoluer", width=20, command=action_bouton)
bouton_couleur.pack()
bouton_couleur = Button(root, text="Aleatoire", width=20, command=aleatoire)
bouton_couleur.pack()
bouton_quitter = Button(root, text="Quitter", width=20, command=root.quit)
bouton_quitter.pack()

root.mainloop()

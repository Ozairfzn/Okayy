from random import randint
from tkinter import *


hauteur = 800
p = 100
tableau = [[0 for j in range(p)] for i in range(p)]


def afficher_tableau():
    echelle = hauteur//p
    for i in range(p):
        for j in range(p):
            if tableau[i][j] == 1:
                canvas.create_rectangle(
                    i*echelle, j*echelle, (i+1)*echelle, (j+1)*echelle, fill="green")
            else:
                canvas.create_rectangle(
                    i*echelle, j*echelle, (i+1)*echelle, (j+1)*echelle)


def peut_tomber(i,j):
    if i == p-1:
        return False
    if tableau[i+1][j]:
        return False
    if j != 0 and tableau[i][j-1]:
        return False
    if j != p-1 and tableau[i][j+1]:
        return False
    return True


def faire_tomber(j):
    i = 0
    while peut_tomber(i, j):
        i += 1
    tableau[i][j] = 1



def faire_tomber_hasard(k):
    for _ in range(k):
        b = randint(0, p-1)
        faire_tomber(b)


root = Tk()
canvas = Canvas(root, width=hauteur, height=hauteur, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)


faire_tomber_hasard(5_000)
afficher_tableau()

root.mainloop()

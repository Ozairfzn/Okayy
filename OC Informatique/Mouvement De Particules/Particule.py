from tkinter import *
from math import *


class Particule():
    def __init__(self, x, y, vx, vy, m):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.m = m

    def __str__(self):
        ligne = "("+str(self.x)+", "+str(self.y) + "), (" + \
            str(self.vx)+", "+str(self.vy)+"), "+str(self.m)
        return ligne

    def action_vitesse(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def affiche(self, avec_fleche=False):
        x, y, vx, vy, m = self.x, self.y, self.vx, self.vy, self.m
        i, j = xy_vers_ij(x, y)

        echelle = 1

        if avec_fleche:
            fleche = canvas.create_line(
                i, j, i+vx*echelle, j-vy*echelle, fill="blue", arrow="last", width=4)

        rayon = 6
        disque = canvas.create_oval(
            i-rayon, j-rayon, i+rayon, j+rayon, fill="red")


root = Tk()

Largeur = 800
Hauteur = 600


def xy_vers_ij(x, y):
    return Largeur//2 + x, Hauteur//2 - y


canvas = Canvas(root, width=Largeur, height=Hauteur, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

p = Particule(-300,-100,50,30,10)

for k in range(10):
    p.affiche(avec_fleche=True)
    p.action_vitesse()

root.mainloop()

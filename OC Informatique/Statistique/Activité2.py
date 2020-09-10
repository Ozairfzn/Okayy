from random import *
from tkinter import *


def graphique_barres(liste):
    x = 150
    y = 550
    for i in liste:
        canvas.create_rectangle(x, y, x+20, 550-i*25, fill="red")
        x += 50
    return


def graphique_cumulatif(liste):
    x1 = 150
    x2 = 250
    y = 550
    echelle = 5
    for i in liste:
        canvas.create_rectangle(x1, y, x2, y-i*echelle, fill="purple", width=3)
        y -= i*echelle
    return


def graphique_pourcentage(liste):
    y1 = 275
    y2 = 375
    x = 100
    echelle = 5
    for i in liste:
        canvas.create_rectangle(x, y1, x+i*echelle, y2, fill="purple", width=3)
        x += i*echelle
    return


def graphique_secteurs(liste):
    x1, y1, x2, y2 = 200, 100, 600, 500
    debut_angle = 0
    x = 360/len(liste)
    echelle = (len(liste)*x)/sum(liste)
    for i in liste:
        canvas.create_arc(x1, y1, x2, y2, start=debut_angle,
                          extent=echelle*i, style=PIESLICE)
        debut_angle += echelle*i
    return


liste = [randint(1, 20) for i in range(10)]

root = Tk()
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(fill="both", expand=True)
graphique_secteurs(liste)
root.mainloop()

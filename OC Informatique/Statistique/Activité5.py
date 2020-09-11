from random import *
from tkinter import *


def cours_bourse():
    liste = [1000]
    for i in range(1, 365):
        valeur = randint(-10, 12)/3
        liste.append(valeur+liste[i-1])
    return liste


def moyenne_mobile(liste, duree):
    L = liste[:duree]
    n = len(liste)
    for i in range(duree, n):
        L.append(sum(liste[i-duree: i])/duree)
    return L


def pixel(x, y, couleur):
    canvas.create_rectangle(x, y, x+1, y+1, outline=couleur)
    return


root = Tk()
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(fill="both", expand=True)
liste = cours_bourse()

x = 250
for i in liste:
    pixel(x, 1400-i, "red")
    x += 1

x = 250
for i in moyenne_mobile(liste, 7):
    pixel(x, 1400-i, "blue")
    x += 1

x = 250
for i in moyenne_mobile(liste, 30):
    pixel(x, 1400-i, "brown")
    x += 1

root.mainloop()

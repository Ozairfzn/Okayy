from tkinter import *


def mediane(liste):
    liste = sorted(liste)
    n = len(liste)
    if n % 2 == 0:
        return (liste[n//2-1] + liste[n//2]) / 2
    else:
        return liste[(n-1)//2]


def notes_vers_liste(effectif_notes):
    liste = []
    indice = 0
    for i in effectif_notes:
        for j in range(i):
            liste.append(indice)
        indice += 1
    return liste


def calcule_quartiles(liste):
    liste = notes_vers_liste(liste)
    n = len(liste)
    Q1 = mediane(liste[:n//2])
    Q2 = mediane(liste)
    Q3 = mediane(liste[n//2:])

    return Q1, Q2, Q3


def diagramme_boite(effectif_notes):
    x = 50
    y = 250
    for i in effectif_notes:
        canvas.create_rectangle(x, y, x+20, y-i*25, fill="red")
        x += 50
    return


root = Tk()
canvas = Canvas(root, width=1200, height=300, background="white")
canvas.pack(fill="both", expand=True)
diagramme_boite([0, 0, 0, 0, 0, 1, 0, 2, 0, 1,
                 5, 1, 2, 3, 2, 4, 1, 2, 0, 1, 0])

root.mainloop()

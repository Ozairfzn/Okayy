from tkinter import *


def f(z, c): return z**2 + c


def iterer(c):
    maxiter = 100
    z = 0
    i = 1

    while abs(z) <= 2 and i < maxiter:
        z = f(z, c)
        i += 1

    if maxiter == i:
        return 0
    return i


def afficher_pixel(i, j, couleur):
    canvas.create_line(i, j, i, j+1, fill=couleur)


def choix_couleur(i):
    if i == 0:
        R, G, B = 0, 0, 0
    else:
        R, G, B, = 255, 125+i, 125+i

    return '#%02x%02x%02x' % (R, G, B)


xmin, xmax, ymin, ymax = -2.2, 1, -1.2, 1.2
Nx = 800
Ny = round((ymin-ymax) / (xmin-xmax) * Nx)


def mandelbrot():
    pasx, pasy = (xmax-xmin)/Nx, (ymax-ymin)/Ny
    a, b = xmin, ymin

    for i in range(Nx):
        for j in range(Ny):
            c = a + b*1j
            vitesse = iterer(c)
            afficher_pixel(i, j, choix_couleur(vitesse))
            b += pasy
        b = ymin
        a += pasx


root = Tk()
canvas = Canvas(root, width=Nx, height=Ny, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

mandelbrot()

root.mainloop()

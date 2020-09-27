from tkinter import *
import math


class TortueBasique:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.trace = True
        self.couleur = "red"

    def renvoyer_xy(self):
        return self.x, self.y

    def aller_a_xy(self, x, y):
        x0 = self.x
        y0 = self.y
        self.x = x
        self.y = y
        if self.trace:
            canvas.create_line(x0, y0, x, y, fill=self.couleur, width=3)
        return

    def abaisser_stylo(self):
        self.trace = True

    def relever_stylo(self):
        self.trace = False

    def changer_couleur(self, couleur):
        self.couleur = couleur


class TortueTournante(TortueBasique):
    def __init__(self):
        TortueBasique.__init__(self)
        self.direction = 0

    def fixer_direction(self, direction):
        self.direction = direction

    def tourner(self, angle):
        self.direction += angle

    def avancer(self, longueur):
        x = longueur*math.cos((2*math.pi)/(360)*self.direction)
        y = longueur*math.sin((2*math.pi)/(360)*self.direction)
        self.aller_a_xy(self.x+x, self.y+y)

    def sorienter_vers(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        angle = (360/(2*math.pi))*math.atan2(y2-y1, x2-x1)
        self.direction = angle


root = Tk()
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

tortue1 = TortueTournante()

tortue2 = TortueTournante()
tortue2.changer_couleur('blue')
tortue2.relever_stylo()
tortue2.aller_a_xy(500, 1)
tortue2.abaisser_stylo()
tortue2.fixer_direction(50)

for i in range(400):
    tortue2.avancer(1)
    tortue1.sorienter_vers(tortue2)
    tortue1.avancer(2)
root.mainloop()

root.mainloop()

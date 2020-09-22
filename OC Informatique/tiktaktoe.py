import os
import random


x = "X"
o = "O"
vide = " "
jeu = [[vide, vide, vide],
       [vide, vide, vide],
       [vide, vide, vide]]

print(f" -1- -2- -3-\n| {jeu[0][0]} | {jeu[0][1]} | {jeu[0][2]} |\n -4- -5- -6-\n| {jeu[1][0]} | {jeu[1][1]} | {jeu[1][2]} |\n -7- -8- -9-\n| {jeu[2][0]} | {jeu[2][1]} | {jeu[2][2]} |\n --- --- ---\n")


def gagnat(t):
    for i in range(3):
        if (t[i][0] == t[i][1] and t[i][0] == t[i][2]) and t[i][0] != vide:
            return True
        elif (t[0][i] == t[1][i] and t[0][i] == t[2][i]) and t[0][i] != vide:
            return True
    if (t[0][0] == t[1][1] and t[1][1] == t[2][2]) and t[1][1] != vide:
        return True
    elif (t[2][0] == t[1][1] and t[1][1] == t[0][2]) and t[1][1] != vide:
        return True
    somme = 0
    for i in t:
        for j in i:
            if j != vide:
                somme += 1
    if somme == 9:
        return True
    return False


def gagnat_print(t):
    for i in range(3):
        if (t[i][0] == t[i][1] and t[i][0] == t[i][2]) and t[i][0] != vide:
            return t[i][0]
        elif (t[0][i] == t[1][i] and t[0][i] == t[2][i]) and t[0][i] != vide:
            return t[0][i]
    if (t[0][0] == t[1][1] and t[1][1] == t[2][2]) and t[1][1] != vide:
        return t[1][1]
    elif (t[2][0] == t[1][1] and t[1][1] == t[0][2]) and t[1][1] != vide:
        return t[1][1]


tour = 0
while not gagnat(jeu):
    if tour == 0:
        pos = int(input("Joueur 'X': ")) - 1
        while pos not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            pos = int(input("Joueur 'X': ")) - 1
        while jeu[pos//3][pos % 3] != vide:
            pos = int(input("Joueur 'X': ")) - 1
        jeu[pos//3][pos % 3] = x
        tour += 1

    elif tour == 1:
        pos = int(input("Joueur 'O': ")) - 1
        while pos not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            pos = int(input("Joueur 'O': ")) - 1
        while jeu[pos//3][pos % 3] != vide:
            pos = int(input("Joueur 'O': ")) - 1
        jeu[pos//3][pos % 3] = o
        tour -= 1
    os.system("cls")
    print(f" -1- -2- -3-\n| {jeu[0][0]} | {jeu[0][1]} | {jeu[0][2]} |\n -4- -5- -6-\n| {jeu[1][0]} | {jeu[1][1]} | {jeu[1][2]} |\n -7- -8- -9-\n| {jeu[2][0]} | {jeu[2][1]} | {jeu[2][2]} |\n --- --- ---\n")


if gagnat_print(jeu) != None:
    print(f"{gagnat_print(jeu)} a gagné(e) !")
else:
    print("Egalité")

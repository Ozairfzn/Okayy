import math
import random
import time
import os


def racine2(n): return round(math.sqrt(2), n)


def trigo(angle): return math.cos(angle)**2 + math.sin(angle)**2


def pari(n):
    for i in range(n):
        if 6 == random.randint(1, 6) and i == n-1:
            return True
    return False


def memory():
    L = []
    while True:
        L.append(random.randint(1, 4))
        os.system("cls")
        print(f"Votre nombre {len(L)}e est {L[-1]}")
        time.sleep(2)
        os.system("cls")

        for i in range(len(L)):
            n = int(input(f"Entrez le {i+1}e nombre: "))
            if n != L[i]:
                return False


def monty_hall():
    Portes = [1, 2, 3]
    voiture = random.choice(Portes)

    choix = int(input("Choissiez entre les portes: "))
    while choix not in Portes:
        choix = int(input("Choissiez entre les portes: "))

    montrer = random.choice(Portes)
    while montrer == voiture or montrer == choix:
        montrer = random.choice(Portes)
    print("La voiture n'est pas derrière la porte", montrer)

    changer = input("Voulez-vous changer de porte ? oui/non: ")
    if changer == "oui":
        if voiture == choix:
            return "Vous avez perdu !"
        else:
            return "Vous avez gagné !"

    elif changer == "non":
        if voiture == choix:
            return "Vous avez gagné !"
        else:
            return "Vous avez perdu !"


def dés(n):
    somme9, somme10 = 0, 0

    for i in range(n):
        somme = 0
        for j in range(3):
            somme += random.randint(1, 6)

        if somme == 9:
            somme9 += 1
        elif somme == 10:
            somme10 += 1

    return f"9:  {somme9/n*100}%\n10: {somme10/n*100}%"

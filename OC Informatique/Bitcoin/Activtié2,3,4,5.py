import random


def addition(liste1, liste2):
    for i in range(len(liste1)):
        liste1[i] = (liste1[i] + liste2[i]) % 100
    return liste1


def est_plus_petit(liste, liste_max):

    if len(liste) < len(liste_max):
        x = len(liste)
    else:
        x = len(liste_max)

    for i in range(x):
        if liste[i] > liste_max[i]:
            return False
    return True


def phrase_vers_liste(phrase):
    L = []
    for i in phrase:
        L.append(ord(i) % 100)
    x = len(phrase) % 6
    for i in range(6-x):
        L.insert(0, 0)
    return L


def un_tour(bloc):
    premier = [7, 11, 13, 17, 19, 23]

    for i in range(len(bloc)):
        if i % 2 == 1:
            bloc[i] += bloc[i-1]

    for i in range(len(bloc)):
        bloc[i] = bloc[i] * premier[i] + 1
        bloc[i] %= 100

    bloc.insert(0, bloc.pop(5))
    return bloc


def dix_tours(bloc):
    for i in range(10):
        bloc = un_tour(bloc)
    return bloc


def liste_6(liste):
    res = []
    n_listes = len(liste)//6
    for i in range(n_listes):
        res.append(liste[:6])
        liste = liste[6:]
    return res


def hachage(liste):
    liste = liste_6(liste)
    n = len(liste)
    for i in range(n-1):
        liste[0] = dix_tours(liste[0])
        liste[1] = addition(liste[0], liste[1])
        liste.pop(0)
    liste[0] = dix_tours(liste[0])
    return liste[0]


def verification_preuve_de_travail(liste, preuve, max):
    for i in preuve:
        liste.append(i)
    liste = hachage(liste)
    return est_plus_petit(liste, max)


def preuve_de_travail(liste, max):
    for i in range(10000):
        preuve = [random.randint(0, 99) for i in range(6)]
        if verification_preuve_de_travail(liste, preuve, max):
            return preuve
    return None


global Livre
Livre = [[0, 0, 0, 0, 0, 0]]


def ajout_transaction(transaction):
    Livre.append(transaction)


def minage():
    liste = phrase_vers_liste(Livre[-1])
    liste = preuve_de_travail(liste, [0, 50, 99])
    Livre.append(liste)


ajout_transaction("Ozair -100")
minage()
print(Livre)

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


def hachage(liste):
    


print(hachage([0, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10]))
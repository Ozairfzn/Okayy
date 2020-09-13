def decimale_vers_entier(liste_decimale):
    n = len(liste_decimale)-1
    res = 0
    for i in liste_decimale:
        res += i*(10**n)
        n -= 1
    return res


def binaire_vers_entier(liste_binaire):
    n = len(liste_binaire)-1
    res = 0
    for i in liste_binaire:
        res += i*(2**n)
        n -= 1
    return res


def binaire_vers_entier_bis(liste_binaire):
    n = 0
    for i in liste_binaire:
        if i == 0:
            n *= 2
        else:
            n = 2*n + 1
    return n


def entier_vers_basse_B(n, b):
    L = []
    while n != 0:
        L.insert(0, n % b)
        n //= b
    return L


def palindrome(liste):
    return liste == list(reversed(liste))


def NON(liste_binaire):
    for i in range(len(liste_binaire)):
        if liste_binaire[i] == 0:
            liste_binaire[i] = 1
        else:
            liste_binaire[i] = 0
    return liste_binaire


def ajouter_zeros(liste, p):
    while len(liste) != p:
        liste.insert(0, 0)
    return liste


def OU(liste1, liste2):
    if len(liste1) > len(liste2):
        liste2 = ajouter_zeros(liste2, len(liste1))
    elif len(liste1) < len(liste2):
        liste1 = ajouter_zeros(liste1, len(liste2))
    for i in range(len(liste1)):
        if liste1[i] == 1 or liste2[i] == 1:
            liste1[i] = 1
        elif liste1[i] == 0 and liste2[i] == 0:
            liste1[i] = 0
    return liste1


def ET(liste1, liste2):
    if len(liste1) > len(liste2):
        liste2 = ajouter_zeros(liste2, len(liste1))
    elif len(liste1) < len(liste2):
        liste1 = ajouter_zeros(liste1, len(liste2))
    for i in range(len(liste1)):
        if liste1[i] == 1 and liste2[i] == 1:
            liste1[i] = 1
        else:
            liste1[i] = 0
    return liste1


def tous_les_binaires(p):
    L = []
    for i in range(2**p):
        L.append(ajouter_zeros(entier_vers_basse_B(i, 2), p))
    return L

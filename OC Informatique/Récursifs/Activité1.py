def somme_carres_R(n):
    if n == 1:
        return 1
    else:
        return somme_carres_R(n-1) + n**2


def inverseR(L, LR=[]):
    if len(L) == 0:
        return L
    LR.append(L[-1])
    inverseR(L[:-1], LR)
    return LR


def LePlusGrandR(L):
    if len(L) == 1:
        return L[0]

    premier = L[0]
    Max = LePlusGrandR(L[1:])

    if premier > Max:
        plus_grand = premier
    else:
        plus_grand = Max

    return plus_grand


chaine_binaire = ""


def binaireR(n):
    global chaine_binaire
    if n == 0:
        chaine_binaire += "0"
        return
    elif n == 1:
        chaine_binaire += "1"
        return

    binaireR(n//2)

    if n % 2 == 0:
        chaine_binaire += "0"
    else:
        chaine_binaire += "1"
    return chaine_binaire

def arrondi(n):
    y = int(1000*n)
    z = y % 100
    if z >= 50:
        t = (y // 100 + 1) / 10
    else:
        t = (y // 100) / 10
    return t


def moy(L):
    somme = 0
    for i in L:
        somme += i
    return arrondi(somme / len(L))

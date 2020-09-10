def moyenne(liste):
    return sum(liste)/len(liste)


def variance_écart(liste):
    m = moyenne(liste)
    n = len(liste)
    v = 0
    for i in range(n):
        v += (liste[i] - m) ** 2
    v /= n
    return (f"la variance faut {v} et l'écart faut {v**(1/2)}")

def nbr_liste(n):
    return [int(i) for i in str(n)]


def nps(n):
    s = nbr_liste(n)
    p = len(s)
    for i in s:
        if i == 0 or i == 1:
            p -=1
    if p == 0:
        return False
    k = 1
    while True:
        somme = 0
        for i in s:
            g = i**k
            somme += g
        if somme > n:
            return False
        if somme+1 == n or somme-1 == n:
            return True
        k += 1



def S(d):
    res = 0
    for i in range(10**d):
        if nps(i):
            res += i
    return res


print(S(6))

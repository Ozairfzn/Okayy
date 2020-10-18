from math import sqrt, floor


def premier(p):
    if p == 2:
        return True
    elif p < 2:
        return False
    elif p % 2 == 0:
        return False
    n = int(sqrt(p))
    for i in range(3, n, 2):
        if p % i == 0:
            return False
    return True


def nombre_solutions_goldbach(n):
    for p in range(2, n//2+1):
        if premier(p):
            q = n - p
            if p <= q and premier(q):
                print(f"{n} = {p} + {q}")


def nombre_de_diviseurs(n):
    L = []
    for i in range(1, n//2+1):
        if n % i == 0:
            L.append(i)
    L.append(n)
    return len(L)


def quatre_et_huit_diviseurs(Nmin, Nmax):
    n4 = 0
    n8 = 0
    for i in range(Nmin, Nmax+1):
        if nombre_de_diviseurs(i) == 4:
            n4 += 1
        elif nombre_de_diviseurs(i) == 8:
            n8 += 1
    return(n4, n8)


def racine(n):
    return floor(sqrt(n))


def racine_2(n):
    p = 0
    while True:
        if p**2 >= n:
            return p-1
        p += 1


def racine_3(n):
    a, b = 1, n
    while abs(a-b) > 1:
        a = (a+b)//2
        b = n//a
    return min(a, b)

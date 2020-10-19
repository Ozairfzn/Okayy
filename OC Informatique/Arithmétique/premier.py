from math import sqrt


def premier(p):
    if p == 2:
        return True
    elif p < 2:
        return False
    elif p % 2 == 0:
        return False
    n = int(sqrt(p))+1
    for i in range(3, n, 2):
        if p % i == 0:
            return False
    return True


Liste_premiers = [2, 3]

for i in range(0, 1_000_000, 6):
    if premier(i-1):
        Liste_premiers.append(i-1)
    if premier(i+1):
        Liste_premiers.append(i+1)

print(Liste_premiers)

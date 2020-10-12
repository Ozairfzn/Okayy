import random

liste = [random.randint(0, 1000) for i in range(10)]
cliste = list(liste)

n = len(cliste)

for i in range(n):
    rg_min = i
    for j in range(1+i, n):
        if cliste[j] < cliste[rg_min]:
            rg_min = j
    cliste[rg_min], cliste[i] = cliste[i], cliste[rg_min]

print(cliste)

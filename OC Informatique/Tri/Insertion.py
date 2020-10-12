import random

liste = [random.randint(0, 1000) for i in range(10)]
cliste = list(liste)

n = len(cliste)

for i in range(n):
    el = liste[i]
    
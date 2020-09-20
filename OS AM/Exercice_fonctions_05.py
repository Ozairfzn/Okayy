# a)
def sommeA(x, r, n):
    somme = 0
    chaine = ""
    for terme in range(n+1):
        somme += x + terme*r
        chaine += f"({x}+{terme}*{r})"
    return somme, chaine


# b)
def sommeG(x, q, n):
    somme = 0
    chaine = ""
    for terme in range(n+1):
        somme += x*q**terme
        chaine += f"{x}*{q}^{terme}  "
    return somme, chaine


# c)
  # 1)    print(sommeA(1, 2, 8))
  # 2)    print(sommeA(0 ,5, 20))
  # 3)    print(sommeG(1, 2, 10))
  # 4)    Imppossible car n E N

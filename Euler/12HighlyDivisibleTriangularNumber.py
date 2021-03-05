def nbr_diviseurs(n):
    res = 0
    p = int(n**0.5)+1
    for i in range(1, p):
        if n%i == 0:
            res += 2
    return res

somme = 0
for i in range(1, 12_376):
    somme += i
    if nbr_diviseurs(somme) > 500:
        print(somme)
        break

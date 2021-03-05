def premier(p):
    n = int((p)**0.5)+1
    for i in range(3, n, 2):
        if p % i == 0:
            return False
    return True


somme = 5
for i in range(6, 2_000_000, 6):
    if premier(i+1):
        somme += i+1
    if premier(i-1):
        somme += i-1

print(somme)
# 142913828922

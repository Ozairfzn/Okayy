def diviseurs(n):
    L = []
    for i in range(1, n+1):
        if n % i == 0:
            L.append(i)
    return L

# 2**19 - 1, 2**31 - 1,

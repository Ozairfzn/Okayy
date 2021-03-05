def syracuse(u):
    L = 1
    while u != 1:
        L += 1
        if u % 2 == 0:
            u //= 2
        else:
            u = 3*u+1
    return L

# 35655
a = 35655
for i in range(1, 1_000_000):
    if syracuse(i) > a:
        a = i
print(a)

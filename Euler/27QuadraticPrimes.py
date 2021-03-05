import numpy as np


def premier(p):
    if p == 2:
        return True
    elif p < 2:
        return False
    elif p % 2 == 0:
        return False
    n = int(p**0.5)+1
    for i in range(3, n, 2):
        if p % i == 0:
            return False
    return True


a = np.linspace(-1000, 1000, 2001)
b = np.linspace(-1000, 1000, 2001)
m = 0
a1, b1 = 0, 0

for i in a:
    for j in b:
        n = 0
        while premier(n*n + i*n + j):
            n += 1
        if n > m:
            m = n
            a1, b1 = i, j


print(m, a1, b1)
# -61, 971

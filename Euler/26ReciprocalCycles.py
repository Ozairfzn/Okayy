from decimal import *

getcontext().prec = 2000


def chaine(d):
    frac = Decimal(10**(len(str(d))-1))/Decimal(d)
    return str(frac-int(frac))[2:-1]


def sub(chaine, sub):
    s = len(sub)
    res = []
    for i in range(0, len(chaine)-s):
        if chaine[i:i+s] == sub:
            res.append(i)
    return res


def diff(L):
    if len(L) < 3:
        return 0
    if L[1] - L[0] == L[2] - L[1]:
        return L[1] - L[0]


m = 0
index = 0
for i in range(1, 1001):
    d = chaine(i)
    n = (diff(sub(d, d[5:8])))
    if n > m:
        m = n
        index = i

print(m, index)
# 983

"""
10001st prime
Problem 7
"""


def prime(p):
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


p = 2
i = 3

while p < 10001:
    if prime(i):
        p += 1
    i += 2


print(i)

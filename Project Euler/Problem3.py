"""
Largest prime factor
Problem 3

What is the largest prime factor of the number 600851475143 ?
"""


def prime_factors(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    p = int(n**0.5)+1
    L = []
    if n % 2 == 0:
        L.append(2)
    for i in range(3, p, 2):
        if n % i == 0:
            L.append(i)
    return L


p = prime_factors(600851475143)

print(p[:len(p)//2+1])

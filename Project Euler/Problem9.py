"""
Special Pythagorean triplet
Problem 9
"""

m = 10000
n = 100000

while True:
    for a in range(m, n):
        for b in range(m, n):
            for c in range(m, n):
                if (c**2 == a**2+b**2) and (a < b) and (a+b+c == 1000):
                    print(a, b, c)

    m, n = n, n*10

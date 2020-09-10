import time


def verification(x, y, p):
    return (x**2) % p == y


t1 = time.time()
x = 0
while True:
    if verification(x, 17, 101):
        print(x)
        break
    x += 1
t2 = time.time()

print(t2-t1)


def racine_approchee(x, y, p, marge):
    return (x**2 - y) % p <= marge


t3 = time.time()
x = 0
while True:
    if racine_approchee(x, 8371779, 32416187567, 200):
        print(x)
        break
    x += 1
t4 = time.time()

print(t4-t3)

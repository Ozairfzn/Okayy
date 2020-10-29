"""
Smallest multiple
Problem 5

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def div(n):
    L = []
    for i in range(1, 21):
        if n % i == 0:
            L.append(i)
    return L


i = 200000000
while True:
    if len(div(i)) == 20:
        print(i)
        break
    i += 20

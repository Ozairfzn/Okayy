"""
Even Fibonacci numbers
Problem 2
"""

summ = 0
a, b = 1, 2

for i in range(30):
    summ += a
    a, b = b, a+b

print(summ)

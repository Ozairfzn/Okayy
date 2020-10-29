"""
Largest palindrome product 
Problem 4

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindrome(w): return w == w[::-1]


largest = 0

for a in range(100):
    for b in range(100):
        for c in range(100):
            p = a*b*c
            if p > largest and palindrome(str(p)):
                largest = p

print(largest)

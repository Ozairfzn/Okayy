# Exercice 2
def trois_cinq(a, b):
    sommea = 0
    sommeb = 0
    for i in range(a, b+1):
        if i % 5 == 0 and i % 3 == 0:
            sommea += i
        if i % 5 == 0 or i % 3 == 0:
            sommeb += i
    return sommea, sommeb

# Exercice 3
def ppmc(a, b):
    plus_grand = max(a, b)
    i = plus_grand
    while True:
        if i % a == 0 and i % b == 0:
            return i
        i += plus_grand

# Exercice 4
def tab(a, b):
    for i in range(a, b+1):
        print(f"f({i}) = {i**2 - 2*i - 2}")
    return

# Exercice 5
def triangle(n):
    n += 1
    for i in range(1, n):
        print((n-i)*" "+i*"*", end="")
        print(i*"*"+(n-i)*" ")

    for i in range(1, n):
        print(i*" "+(n-i)*"*", end="")
        print((n-i)*"*"+i*" ")
    return " "

# Exercice 6
def astérisque(chaine):
    res = ""
    for i in chaine:
        res += (i+"*")
    return res[:-1]

# Exercice 7
def inverse1(chaine):
    res = ""
    for i in chaine:
        res = i + res
    return res


def inverse2(chaine):
    res = ""
    i = 0
    while i < len(chaine):
        res = chaine[i] + res
        i += 1
    return res

# Exercice 8
def remplace_e(chaine):
    res = ""
    for i in chaine:
        if i != "e":
            res += i
        else:
            res += "*"
    return res

# Exercice 9
def palindrome(mot):
    return mot == inverse1(mot)

# Exercice 10
def rebond(h1, h2, f):
    res = 0
    while h1 >= h2:
        res += 2
        h1 = h1-(h1/f)
    return res

# Exercice 11
def triplet_pythagor(n):
    L = []
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if (c**2 == a**2+b**2) and (a != b and b != c and a != c) and (a < b):
                    L.append((a,b,c))
    return L 

# Exercice 12
def syracuse(u):
    L = []
    while u != 1:
        L.append(u)
        if u % 2 == 0:
            u //= 2
        else:
            u = 3*u+1
    return L


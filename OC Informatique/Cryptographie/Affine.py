Alphabet = ""
for i in range(65, 91):
    Alphabet += chr(i)


def affine(phrase, a, b):
    res = ""
    for i in phrase:
        if i in Alphabet:
            res += Alphabet[(a * Alphabet.index(i) + b) % 26]
        else:
            res += i
    return res


def inv_mod(a,n):
    for b in range (1,n):
        if (a*b)%n==1:
            return b


def deaffine(phrase, a, b):
    res = ""
    for i in phrase:
        if i in Alphabet:
            res += Alphabet[((Alphabet.index(i) - b) * inv_mod(a, 26)) % 26]
        else:
            res += i
    return res


a_possible = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def attaque_affine(phrase):
    for a in a_possible:
        for b in range(1, 26):
            print(a, b, deaffine(phrase, a, b))
    return

attaque_affine("OIDABZVQVTEMDTGDZNUV") # 11, 3

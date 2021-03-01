Alphabet = ""
for i in range(65, 91):
    Alphabet += chr(i)


def chiffre_cesar_phrase(phrase, k):
    res = ""
    for i in phrase:
        if i in Alphabet:
            res += Alphabet[(Alphabet.index(i) + k) % 26]
        else:
            res += i
    return res


def dechiffre_cesar_phrase(phrase, k):
    res = ""
    for i in phrase:
        if i in Alphabet:
            res += Alphabet[(Alphabet.index(i) - k) % 26]
        else:
            res += i
    return res


def attaque_cesar(phrase):
    for i in range(26):
        print(i, chiffre_cesar_phrase(phrase, i))

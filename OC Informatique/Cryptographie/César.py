Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def chiffre_cesar_caractere(car, k):
    return Alphabet[(Alphabet.index(car) + k) % 26]


def chiffre_cesar_phrase(phrase, k):
    res = ""
    for i in phrase:
        if i in Alphabet:
            res += chiffre_cesar_caractere(i, k)
        else:
            res += i
    return res


def attaque_cesar(phrase):
    for i in range(26):
        print(i, chiffre_cesar_phrase(phrase, i))


attaque_cesar("HSFGJSEAP F S HDMK VW HGLAGF")

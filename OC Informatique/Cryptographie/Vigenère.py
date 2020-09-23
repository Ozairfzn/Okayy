Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def chiffre_cesar_caractere(car, k):
    return Alphabet[(Alphabet.index(car) + k) % 26]


def chiffre_vigenere(phrase, cle):
    res = ""
    indice = 0
    for i in phrase:
        if i in Alphabet:
            res += chiffre_cesar_caractere(i, cle[indice % 3])
            indice += 1
        else:
            res += i
    return res

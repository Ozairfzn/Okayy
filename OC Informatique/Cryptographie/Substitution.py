Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Melange = "ykcodmfjgzaxrnbutqiphwesvl"


def substitution(phrase, Alphabet_depart, Alphabet_arrivee):
    res = ""
    for i in phrase:
        if i in Alphabet_depart:
            res += Alphabet_arrivee[Alphabet_depart.index(i)]
        else:
            res += i
    return res


def statistiques(phrase):
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = [0 for i in range(26)]
    for i in phrase:
        if i in Alphabet:
            res[Alphabet.index(i)] += 1
    return res


def affiche_statistiques(phrase):
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    stat = statistiques(phrase)
    for i in range(len(Alphabet)):
        print(f"{Alphabet[i]} --> {stat[i]}")


def frequences(phrase):
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = [0 for i in range(26)]
    for i in phrase:
        if i in Alphabet:
            res[Alphabet.index(i)] += 1
    for i in range(len(res)):
        res[i] = (res[i]/len(phrase)) * 100
    return res


def affiche_frequences(phrase):
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    stat = frequences(phrase)
    for i in range(len(Alphabet)):
        print(f"{Alphabet[i]} --> {stat[i]}")

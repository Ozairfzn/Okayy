import matplotlib.pyplot as plt


Alphabet = ""
for i in range(65, 91):
    Alphabet += chr(i)

Melange = 'QWERTZUIOPASDFGHJKLYXCVBNM'


def substitution(phrase, Alphabet_depart, Alphabet_arrivee):
    res = ""
    for i in phrase:
        if i in Alphabet_depart:
            res += Alphabet_arrivee[Alphabet_depart.index(i)]
        else:
            res += i
    return res


def frequences(phrase):
    res = [0 for i in range(26)]
    for i in phrase:
        if i in Alphabet:
            res[Alphabet.index(i)] += 1
    for i in range(26):
        res[i] /= len(phrase)
    return res


def graphique(phrase):
    frequ_lettres_Fr = [0.0808, 0.0106, 0.0303, 0.0418, 0.1726, 0.0112, 0.0127, 0.0092, 0.0734, 0.0031, 0.0005, 0.0601,
                        0.0296, 0.0713, 0.0526, 0.0301, 0.0099, 0.0655, 0.084, 0.0707, 0.0574, 0.0132, 0.0004, 0.0045, 0.0030, 0.0012]
    plt.figure(figsize=(12, 6), dpi=100)

    for k in range(26):
        p1, = plt.plot(
            [k-0.2, k-0.2], [0, frequences(phrase)[k]], 'r-', linewidth=10)
        p2, = plt.plot([k+0.2, k+0.2], [0, frequ_lettres_Fr[k]],
                       'g-', linewidth=10)

    plt.xlabel("Lettres")
    plt.ylabel("Frequences")
    plt.xticks([k for k in range(26)], [chr(k+65) for k in range(26)])
    plt.legend([p1, p2], ['rouge (freq. lettres texte chiffre)',
                          'vert (freq. th. lettres francais)'])
    plt.show()


def sub_lettre(phrase, lettre_init, lettre_finale):
    res = ""
    for i in phrase:
        if i == lettre_init:
            res += lettre_finale
        else:
            res += i
    return res

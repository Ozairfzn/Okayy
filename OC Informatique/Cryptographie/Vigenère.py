def chiffre_vigenere(phrase, mot_cle):
    cle = []
    for i in mot_cle:
        cle.append(ord(i)-65)
    
    res = ""
    k = 0
    for i in phrase:
        res += chr((ord(i)-65 + cle[k%len(cle)]) % 26 + 65)
        k += 1
    
    return res



def dechiffre_vigenere(phrase, mot_cle):
    cle = []
    for i in mot_cle:
        cle.append(-(ord(i)-65))
    
    res = ""
    k = 0
    for i in phrase:
        res += chr((ord(i)-65 + cle[k%len(cle)]) % 26 + 65)
        k += 1
    
    return res


def mot_prob(phrase, mot):
    m = len(mot)
    for i in range(len(phrase)-m):
        mot_cle = ""
        for j in range(m):
            mot_cle += chr((ord(phrase[i+j]) - ord(mot[j])) % 26 + 65)
        print(mot_cle)


mot_prob("WOLVIIXNJVCORUEHDVXLVQBRJTKDYHNCVPIGRNGHZGNSZPXBATRQBRB", "ATTAQUE")
# jardin

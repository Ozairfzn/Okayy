def input_nombre(text):
    while True:
        try:
            x = eval(input(text))
            if isinstance(x, int) or isinstance(x, float):
                return x
            print("Oops! Il y a eu une erreur.")
        except (ValueError, NameError):
            print("Oops! Il y a eu une erreur.")


def input_entier(text):
    while True:
        try:
            x = int(input(text))
            return x
        except (ValueError, NameError):
            print("Oops! Il y a eu une erreur.")


def demander_polynome(nom):
    deg = -1
    while deg < 0:
        deg = input_entier(f"Entrer le degré du polynôme {nom}(x): ")
    polynome = []

    for i in range(deg+1):
        coefficient = input_nombre(f"Entrer le coefficient du degré {i}: ")
        polynome.append(coefficient)

    return polynome


def afficher_polynome(polynome):
    résultat = ""
    deg = len(polynome) - 1

    for i in range(deg, 1, -1):
        coefficient = polynome[i]
        if coefficient == 0:
            pass
        elif coefficient == 1:
            résultat = f"{résultat} + x^{i}"
        else:
            résultat = f"{résultat} + ({(coefficient)}) x^{i}"

    if polynome[0] == 0 and polynome[1] == 0:
        pass
    elif polynome[1] == 0:
        résultat += f" + ({polynome[0]})"
    elif polynome[0] == 0:
        résultat += f" + ({polynome[1]}) x"
    else:
        résultat += f" + ({polynome[1]}) x + ({polynome[0]})"

    print(résultat[3:])


def polynome_sans_0s_inutiles(polynome):
    while polynome[-1] == 0:
        polynome.pop(-1)
    return polynome


def polynome_meme_taille(polynome1, polynome2):
    if len(polynome1) > len(polynome2):
        while len(polynome1) > len(polynome2):
            polynome2.append(0)

    elif len(polynome1) < len(polynome2):
        while len(polynome1) < len(polynome2):
            polynome1.append(0)

    return polynome1, polynome2


def additionner_deux_polynômes(polynome1, polynome2):
    p1, p2 = list(polynome1), list(polynome2)
    p1, p2 = polynome_meme_taille(p1, p2)

    résultat = []
    for i in range(len(p1)):
        résultat.append(p1[i] + p2[i])

    return résultat


def soustraire_deux_polynômes(polynome1, polynome2):
    p1, p2 = list(polynome1), list(polynome2)
    p1, p2 = polynome_meme_taille(p1, p2)

    résultat = []
    for i in range(len(p1)):
        résultat.append(p1[i] - p2[i])

    return résultat


def multiplier_deux_polynômes(polynome1, polynome2):
    degRes = len(polynome1)-1 + len(polynome2)-1
    résultat = [0 for _ in range(degRes+1)]

    for i in range(len(polynome1)):
        for j in range(len(polynome2)):
            résultat[i + j] += polynome1[i] * polynome2[j]

    return résultat


def evaluer_polynome(polynome, point):
    résultat = 0

    for i in range(len(polynome)):
        coefficient = polynome[i]
        résultat += coefficient * point**i

    return résultat


def tableau_valeurs(polynome, borne_inférieur, borne_supérieur, pas):
    while borne_inférieur <= borne_supérieur:
        print(borne_inférieur, evaluer_polynome(polynome, borne_inférieur))
        borne_inférieur += pas


def racines_rationnelles(polynome):
    a0 = abs(polynome[0])
    an = abs(polynome[-1])

    diva0 = []
    divan = []
    for i in range(1, a0+1):
        if a0 % i == 0:
            diva0.append(i)
            diva0.append(-i)
    for i in range(1, an+1):
        if an % i == 0:
            divan.append(i)
            divan.append(-i)

    racine_possibe = []
    for i in divan:
        for j in diva0:
            racine_possibe.append(j/i)

    racine_rationnelle = []
    for i in racine_possibe:
        if evaluer_polynome(polynome, i) >= -0.0000000001 and evaluer_polynome(polynome, i) <= 0.0000000001:
            racine_rationnelle.append(i)

    return list(set(racine_rationnelle))


def schéma_de_Horner(polynome, monome):
    Q = [polynome[-1]]
    facteur = -monome[0] / monome[1]

    for i in range(len(polynome)-2, -1, -1):
        Q.insert(0, facteur*Q[0] + polynome[i])

    return Q[1:], Q[0]


def division_euclidienne(polynome1, polynome2):
    p1 = list(polynome1)
    p2 = list(polynome2)
    Q = []

    if len(polynome1) < len(polynome2):
        return polynome1, polynome2, [0, 0]

    while len(p1) >= len(p2):
        q = [0 for i in range(len(p1))]
        q[len(p1)-len(p2)] = p1[-1]/p2[-1]

        Q.insert(0, p1[-1]/p2[-1])

        p1 = polynome_sans_0s_inutiles(soustraire_deux_polynômes(
            p1, (multiplier_deux_polynômes(p2, q))))

    return Q, p2, p1


def factoriser(polynome):
    sol = racines_rationnelles(polynome)
    res = []
    for i in sol:
        polynome = schéma_de_Horner(polynome, [i, 1])[0]
        res.append([i, 1])
    res.append(polynome)
    return res


def limites_polynomes_infini(polynome):
    if polynome[-1] > 0:
        return "∞"
    else:
        return "-∞"


def limites_fractions_rationnlles_infini(polynome1, polynome2):
    if len(polynome1) < len(polynome2):
        return 0

    elif len(polynome1) > len(polynome2):

        if polynome1[-1] < 0 and polynome2[-1] < 0:
            return "∞"
        elif polynome1[-1] < 0 or polynome2[-1] < 0:
            return "-∞"
        else:
            return "∞"

    else:
        return polynome1[-1]/polynome2[-1]


def limites_fractions_rationnlles(polynome1, polynome2, point):
    if evaluer_polynome(polynome2, point) != 0:
        return evaluer_polynome(polynome1, point) / evaluer_polynome(polynome2, point)

    dx = 0.000001
    a_plus = evaluer_polynome(polynome1, point+dx) / \
        evaluer_polynome(polynome2, point+dx)
    a_moin = evaluer_polynome(polynome1, point-dx) / \
        evaluer_polynome(polynome2, point-dx)

    if a_plus > 10000 and a_moin < 10000 or a_plus < 10000 and a_moin > 10000:
        return "∄"
    elif abs(a_plus - a_moin) < 0.1:
        return round(a_plus + (a_plus - a_moin), 3)
    elif a_plus > 10000 and a_moin > 10000:
        return "∞"
    elif a_plus < 10000 and a_moin < 10000:
        return "-∞"


def dérivée_polynome(polynome):
    dérivée = []

    for i in range(1, len(polynome)):
        dérivée.append(i*polynome[i])

    return dérivée


def dérivée_produit_polynome(polynome1, polynome2):
    return dérivée_polynome(multiplier_deux_polynômes(polynome1, polynome2))


def dérivée_fractions_rationnelles(polynome1, polynome2):
    nom = (soustraire_deux_polynômes(multiplier_deux_polynômes(dérivée_polynome(
        polynome1), polynome2), multiplier_deux_polynômes(dérivée_polynome(polynome2), polynome1)))
    dénom = (multiplier_deux_polynômes(polynome2, polynome2))

    return nom, dénom

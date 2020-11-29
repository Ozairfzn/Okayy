import matplotlib.pyplot as plt


''' ----------------------------------------------------------------------- '''
''' -------------- Debut Partie Fonctions Complémentaire ------------------ '''
''' ----------------------------------------------------------------------- '''


def input_nombre(text):
    ''' Demander à l'utilisateur de rentrer un nombre '''
    while True:
        try:
            x = eval(input(text))
            if isinstance(x, int) or isinstance(x, float):
                return x
            print("Oops! Il y a eu une erreur.")
        except:
            print("Oops! Il y a eu une erreur.")


def input_entier(text):
    ''' Demander à l'utilisateur de rentrer un nombre entier'''
    while True:
        try:
            x = int(input(text))
            return x
        except:
            print("Oops! Il y a eu une erreur.")


def positive(nombre):
    ''' Renvoie True si le nombre est positive et renvoie False s'il est négative'''
    return nombre > 0


def expo(nombre):
    '''Renvoie le nombre sous forme d'exposant'''
    EXPO = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    chaine = ""
    nombre = str(nombre)
    nombre = list(map(int, nombre))
    for i in nombre:
        chaine += EXPO[i]
    return chaine


def polynome_sans_0s_inutiles(polynome):
    '''Renvoie le polynôme sans les zéros avant le coefficent du plus grand dégré'''
    while polynome[-1] == 0:
        polynome.pop(-1)
    return polynome


def polynome_meme_taille(polynome1, polynome2):
    '''Renvoie les deux polynômes de même taille (avec des zéros inutiles dans un des deux polynôme)'''
    if len(polynome1) > len(polynome2):
        while len(polynome1) > len(polynome2):
            polynome2.append(0)

    elif len(polynome1) < len(polynome2):
        while len(polynome1) < len(polynome2):
            polynome1.append(0)

    return polynome1, polynome2


def schéma_de_Horner(polynome, monome):
    '''Effectue la division d'un polynome par un monome'''
    Q = [polynome[-1]]
    facteur = -monome[0] / monome[1]

    for i in range(len(polynome)-2, -1, -1):
        Q.insert(0, facteur*Q[0] + polynome[i])

    return Q[1:], Q[0]


''' ----------------------------------------------------------------------- '''
''' ------------------ Debut Partie Fonctions ----------------------------- '''
''' ----------------------------------------------------------------------- '''


def demander_polynome(nom):
    ''' Demander à l'utilisateur de rentrer un polynôme '''
    deg = -1
    while deg < 0:
        deg = input_entier(f"Entrer le degré du polynôme {nom}(x): ")

    polynome = []
    for i in range(deg+1):
        coefficient = input_nombre(f"Entrer le coefficient du degré {i}: ")
        polynome.append(coefficient)

    return polynome


def afficher_polynome(polynome):
    ''' Affiche le polynôme '''
    resultat = ""
    deg = len(polynome) - 1

    # Pour tous les coefficient > 1
    for i in range(deg, 1, -1):
        coefficient = polynome[i]
        signe = positive(coefficient)

        if coefficient == 0:
            pass
        elif signe:
            if coefficient == 1:
                resultat += f" + x{expo(i)}"
            else:
                resultat += f" + {coefficient}x{expo(i)}"
        else:
            if coefficient == -1:
                resultat += f" - x{expo(i)}"
            else:
                resultat += f" - {abs(coefficient)}x{expo(i)}"

    # Pour x
    if polynome[1] == 0:
        pass
    else:
        if positive(polynome[1]):
            if polynome[1] == 1:
                resultat += f" + x"
            else:
                resultat += f" + {polynome[1]}x"
        else:
            if polynome[1] == -1:
                resultat += f" - x"
            else:
                resultat += f" - {abs(polynome[1])}x "
    # Pour la constante
    if polynome[0] != 0:
        if positive(polynome[0]):
            resultat += f" + {polynome[0]}"
        else:
            resultat += f" - {abs(polynome[0])}"

    # Signe pour le coefficent le plus grand (le début de la chaine)
    if positive(polynome[-1]):
        print(resultat[3:])
    else:
        print(f"-{resultat[3:]}")


def additionner_deux_polynômes(polynome1, polynome2):
    ''' Additionne les deux polynômes '''
    p1, p2 = list(polynome1), list(polynome2)
    p1, p2 = polynome_meme_taille(p1, p2)

    résultat = []
    for i in range(len(p1)):
        résultat.append(p1[i] + p2[i])

    return résultat


def soustraire_deux_polynômes(polynome1, polynome2):
    ''' Soustrait les deux polynômes'''
    p1, p2 = list(polynome1), list(polynome2)
    p1, p2 = polynome_meme_taille(p1, p2)

    résultat = []
    for i in range(len(p1)):
        résultat.append(p1[i] - p2[i])

    return résultat


def multiplier_deux_polynômes(polynome1, polynome2):
    ''' Multipie les deux polynômes'''
    degRes = len(polynome1)-1 + len(polynome2)-1
    résultat = [0 for _ in range(degRes+1)]

    for i in range(len(polynome1)):
        for j in range(len(polynome2)):
            résultat[i + j] += polynome1[i] * polynome2[j]

    return résultat


def evaluer_polynome(polynome, point):
    ''' Evalue le polynôme en un point'''
    résultat = polynome[0]

    for i in range(1, len(polynome)):
        coefficient = polynome[i]
        résultat += coefficient * point**i

    return résultat


def tableau_valeurs(polynome, borne_inférieur, borne_supérieur, pas):
    ''' Calcule un tableau de valeurs du polynôme pour x qui varie entre deux valeurs avec un pas '''
    tab_X = []
    tab_Y = []
    while borne_inférieur <= borne_supérieur:
        tab_X.append(borne_inférieur)
        tab_Y.append(evaluer_polynome(polynome, borne_inférieur))
        borne_inférieur += pas

    return tab_X, tab_Y


def trace_graphique(X, Y):
    ''' Tracer le graphique en fonction du tableau de valeurs X, Y"  '''

    plt.plot(X, Y)
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


def racines_rationnelles(polynome):
    '''Trouve les racine rationnlles d'un polynôme'''
    if len(polynome) == 0:
        return

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


def division_euclidienne(polynome1, polynome2):
    '''Effectue la division euclidienne de polynôme1 par polynôme'''
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

    return p2, Q, p1


def factoriser(polynome):
    '''Renvoie une chaine ou le polynôme initaile est factoriser'''
    sol = racines_rationnelles(polynome)
    res = []

    for i in sol:
        polynome = schéma_de_Horner(polynome, [-i, 1])[0]
        res.append([-i, 1])
    res.append(polynome)

    chaine = ""
    for i in res:
        if len(i) == 1:
            chaine += str(i[0])
        else:
            coef = i[0]
            if coef > 0:
                chaine += f"(x + {coef})"
            else:
                chaine += f"(x - {abs(coef)})"

    return chaine


def factoriser_fractions(polynome1, polynome2):
    '''Renvoie une chaine ou la fraction polynôme initaile est si'''
    sol1 = racines_rationnelles(polynome1)
    res1 = []

    for i in sol1:
        polynome1 = schéma_de_Horner(polynome1, [-i, 1])[0]
        res1.append([-i, 1])
    res1.append(polynome1)

    sol2 = racines_rationnelles(polynome2)
    res2 = []

    for i in sol2:
        polynome2 = schéma_de_Horner(polynome2, [-i, 1])[0]
        res2.append([-i, 1])
    res2.append(polynome2)

    for i in res1:
        if i in res2:
            res1.remove(i)
            res2.remove(i)

    chaine = ""
    for i in res1:
        if len(i) == 1:
            chaine += str(i[0])
        else:
            coef = i[0]
            if coef > 0:
                chaine += f"(x + {coef})"
            else:
                chaine += f"(x - {abs(coef)})"

    chaine += "\n"
    chaine += len(chaine)*"―"
    chaine += "\n"
    for i in res2:
        if len(i) == 1:
            chaine += str(i[0])
        else:
            coef = i[0]
            if coef > 0:
                chaine += f"(x + {coef})"
            else:
                chaine += f"(x - {abs(coef)})"

    return chaine


def limites_polynomes_infini(polynome):
    '''Calcule la limite de polynôme lorsque x tend vers +∞'''
    if len(polynome) == 1:
        return polynome[0]
    if polynome[-1] > 0:
        return "∞"
    else:
        return "-∞"


def limites_fractions_rationnlles_infini(polynome1, polynome2):
    '''Calcule la limite de polynôme1 diviser par polynôme2 lorsque x tend vers +∞'''
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

    if evaluer_polynome(polynome1, point) == 0 and evaluer_polynome(polynome2, point) == 0:
        return evaluer_polynome(dérivée_polynome(polynome1), point) / evaluer_polynome(dérivée_polynome(polynome2), point)

    dx = 0.000001
    a_plus = evaluer_polynome(polynome1, point+dx) / \
        evaluer_polynome(polynome2, point+dx)
    a_moin = evaluer_polynome(polynome1, point-dx) / \
        evaluer_polynome(polynome2, point-dx)

    if (a_plus > 10000 and a_moin < 10000) or (a_plus < 10000 and a_moin > 10000):
        return "∄"
    elif abs(a_plus - a_moin) < 0.1:
        return round((a_plus + a_moin)/2, 3)
    elif a_plus > 10000 and a_moin > 10000:
        return "∞"
    elif a_plus < 10000 and a_moin < 10000:
        return "-∞"


def derivee_polynome(polynome):
    derivee = []

    for i in range(1, len(polynome)):
        derivee.append(i*polynome[i])

    return derivee


def derivee_produit_polynome(polynome1, polynome2):
    return derivee_polynome(multiplier_deux_polynômes(polynome1, polynome2))


def derivee_fractions_rationnelles(polynome1, polynome2):
    nom = (soustraire_deux_polynômes(multiplier_deux_polynômes(derivee_polynome(
        polynome1), polynome2), multiplier_deux_polynômes(derivee_polynome(polynome2), polynome1)))
    denom = (multiplier_deux_polynômes(polynome2, polynome2))

    return nom, denom


''' ----------------------------------------------------------------------- '''
''' ----------------- Debut Partie code principal-------------------------- '''
''' ----------------------------------------------------------------------- '''


MSG = """
Choix 1:  Entrer/modifier une des polynômes donnée. 
Choix 2:  Afficher un des polynômes.
Choix 3:  Additionner les polynômes.
Choix 4:  Soustraire les polynômes.
Choix 5:  Multiplier les polynômes.
Choix 6:  Evaluer un des polynômes en un point.
Choix 7:  Calculer un tableau de valeurs pour un des polynômes.
Choix 8:  Trouver les racines rationnelles.
Choix 9:  Division euclidienne des polynômes.
Choix 10: Factoriser un des polynôme.
Choix 11: Simplifier la fraction des polynômes.
Choix 12: Limite d'un des deux polynôme lorsque x tend vers +∞.
Choix 13: Limite d'une fraction rationnelle lorsque x tend vers +∞.
Choix 14: Limite d'une fraction rationnelle lorsque x tend vers un point.
Choix 15: Calculer la dérivée d'un des deux polynômes.
Choix 16: Calculer la dérivée du produit des deux polynômes.
choix 17: Calculer la dérivée la fraction des deux polynômes.
Choix 18: Quitter le programme.
"""

P_a = [0, 0]
P_b = [0, 0]

while True:
    print(MSG)

    choix = input("Entrer votre choix : ")

    if choix == "1":
        choix_frac = input(
            "Quelle polynôme voulez-vous modifier [A/B] : ").upper()
        if choix_frac == "A":
            P_a = demander_polynome("A")
        elif choix_frac == "B":
            P_b = demander_polynome("B")
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre 'A' ou 'B'")

    elif choix == "2":
        choix_frac = input(
            "Quel polynôme voulez-vous afficher [A/B] : ").upper()
        if choix_frac == "A":
            afficher_polynome(P_a)
        elif choix_frac == "B":
            afficher_polynome(P_b)
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre 'A' ou 'B'")

    elif choix == "3":
        Q = additionner_deux_polynômes(P_a, P_b)
        print("Las somme des deux polynômes vaut : ")
        afficher_polynome(Q)

    elif choix == "4":
        choix_frac = input(
            "1 pour faire A-B\n2 pour faire B-A : ").upper()
        if choix_frac == "1":
            Q = soustraire_deux_polynômes(P_a, P_b)
        elif choix_frac == "2":
            Q = soustraire_deux_polynômes(P_b, P_a)
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre '1' ou '2'")
        afficher_polynome(Q)

    elif choix == "5":
        Q = multiplier_deux_polynômes(P_a, P_b)
        afficher_polynome(Q)

    elif choix == "6":
        choix_frac = input(
            "Quel polynôme voulez-vous evaluer en un point [A/B] : ").upper()
        point = input_nombre("En quel point voulez-vous l'evaluer? : ")
        if choix_frac == "A":
            print(evaluer_polynome(P_a, point))
        elif choix_frac == "B":
            print(evaluer_polynome(P_b, point))
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre 'A' ou 'B'")

    elif choix == "7":
        choix_frac = input(
            "Quel polynôme voulez-vous calculer un tableau de valeurs [A/B] : ").upper()
        x0 = input_nombre('Entrer la plus petite valeur de x : ')
        x1 = input_nombre('Entrer la plus grande valeur de x : ')
        step = input_nombre('Quel est le pas : ')
        if choix_frac == "A":
            X, Y = tableau_valeurs(P_a, x0, x1, step)
        elif choix_frac == "B":
            X, Y = tableau_valeurs(P_b, x0, x1, step)
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre 'A' ou 'B'")
            continue  # permet de directement retourner au début de la boucle

        trace_graphique(X, Y)

    elif choix == "8":
        choix_frac = input(
            "Pour quel polynôme voulez-vous trouver les racines [A/B] : ").upper()
        if choix_frac == "A":
            print(racines_rationnelles(P_a))
        elif choix_frac == "B":
            print(racines_rationnelles(P_b))
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre 'A' ou 'B'")

    elif choix == "9":
        choix_frac = input(
            "1 pour faire A/B\n2 pour faire B/A : ").upper()
        if choix_frac == "1":
            B, Q, R = division_euclidienne(P_a, P_b)
            afficher_polynome(P_a)
            afficher_polynome(B)
            afficher_polynome(Q)
            afficher_polynome(R)
        elif choix_frac == "2":
            B, Q, R = division_euclidienne(P_b, P_a)
            afficher_polynome(P_b)
            afficher_polynome(B)
            afficher_polynome(Q)
            afficher_polynome(R)
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre '1' ou '2'")

    elif choix == "10":
        choix_frac = input(
            "Quel polynôme voulez-vous factorizer [A/B] : ").upper()
        if choix_frac == "A":
            print(factoriser(P_a))
        elif choix_frac == "B":
            print(factoriser(P_b))
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre 'A' ou 'B'")

    elif choix == "11":
        choix_frac = input(
            "1 pour simplifier A/B\n2 pour simplifier B/A : ").upper()
        if choix_frac == "1":
            print(factoriser_fractions(P_a, P_b))
        elif choix_frac == "2":
            print(factoriser_fractions(P_b, P_a))
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre '1' ou '2'")

    elif choix == "12":
        choix_frac = input(
            "Limite de [A/B] : ").upper()
        if choix_frac == "A":
            print(limites_polynomes_infini(P_a))
        elif choix_frac == "B":
            print(limites_polynomes_infini(P_b))
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre 'A' ou 'B'")

    elif choix == "13":
        choix_frac = choix_frac = input(
            "1 pour la limite de A/B \n2 pour la limite de B/A ").upper()
        if choix_frac == "1":
            print(limites_fractions_rationnlles_infini(P_a, P_b))
        elif choix_frac == "2":
            print(limites_fractions_rationnlles_infini(P_b, P_a))
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre '1' ou '2'")

    elif choix == "14":
        choix_frac = choix_frac = input(
            "1 pour la limite de A/B \n2 pour la limite de B/A ").upper()
        point = input_nombre(
            "Vers quel point voulez-vous qu'elle tend vers? : ")
        if choix_frac == "1":
            print(limites_fractions_rationnlles(P_a, P_b, point))
        elif choix_frac == "2":
            print(limites_fractions_rationnlles(P_b, P_a, point))
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre '1' ou '2'")

    elif choix == "15":
        choix_frac = input(
            "Quel polynôme voulez-vous dériver [A/B] : ").upper()
        if choix_frac == "A":
            dx = derivee_polynome(P_a)
            if len(dx) < 2:
                print(dx[0])
            else:
                afficher_polynome(dx)
        elif choix_frac == "B":
            dx = derivee_polynome(P_b)
            if len(dx) < 2:
                print(dx[0])
            else:
                afficher_polynome(dx)
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre 'A' ou 'B'")

    elif choix == "16":
        dx = derivee_produit_polynome(P_a, P_b)
        if len(dx) < 2:
            print(dx[0])
        else:
            afficher_polynome(dx)

    elif choix == "17":
        choix_frac = input(
            "Quel fraction voulez-vous dériver A/B(1) ou B/A(2) : ").upper()
        if choix_frac == "1":
            nom, denom = derivee_fractions_rationnelles(P_a, P_b)
            if len(nom) < 2:
                print(nom[0])
            else:
                afficher_polynome(nom)
            print(7*max(len(nom), len(denom))*"―")
            if len(denom) < 2:
                print(denom[0])
            else:
                afficher_polynome(denom)
        
        elif choix_frac == "2":
            nom, denom = derivee_fractions_rationnelles(P_b, P_a)
            if len(nom) < 2:
                print(nom[0])
            else:
                afficher_polynome(nom)
            print(7*max(len(nom), len(denom))*"―")
            if len(denom) < 2:
                print(denom[0])
            else:
                afficher_polynome(denom)
        else:
            print("Votre choix n'est pas compréhensible, utiliser la lettre '1' ou '2'")

    elif choix == "18":
        break

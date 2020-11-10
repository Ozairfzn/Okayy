from random import randint


def proposition_joueur():
    while True:
        try:
            proposition = list(map(int, input("Votre proposition? ").split()))
            n = len(proposition)
            proposition = [i for i in proposition if 1 <= i <= 6]
            if len(proposition) == 4 and n == 4:
                break
            print("Oops! Il y a eu une erreur.")
            print("Voici un exemple de proposition valide: 4 2 5 1")

        except (ValueError, NameError):
            print("Oops! Il y a eu une erreur.")
            print("Voici un exemple de proposition valide: 4 2 5 1")

    return proposition


def règles():
    chaine = []
    indice_pas_utilisés = []
    copie = list(combinaison)

    for i in range(len(proposition)):
        if proposition[i] == combinaison[i]:
            chaine.append("#")
            copie.remove(proposition[i])
        else:
            indice_pas_utilisés.append(i)

    for i in indice_pas_utilisés:
        if proposition[i] in copie:
            chaine.append("o")
            copie.remove(proposition[i])

    return sorted(chaine)


print("Pouvez-vous trouver ma combinaison de 4 symboles")
print("[chiffres entre 1 et 6 avec repetitions possibles]")
print("en moins de 10 coups? Entrez les symboles des")
print("propositions terminees par [Entree].")
print("(# un bien place, o un mal place)")


combinaison = [randint(1, 6) for _ in range(4)]
proposition = [0, 0, 0, 0]

coup = 10
while proposition != combinaison and coup > 0:
    proposition = proposition_joueur()

    coup -= 1
    print(("".join(règles()) + f" (reste {coup} coups)"))


if coup > 0:
    print(f"Bravo! Vous avez trouvé en {10-coup} coups")
else:
    print("Vous avez perdu!")

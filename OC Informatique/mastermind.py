from random import randint


def proposition_joueur():
    while True:
        try:
            proposition = list(map(int, input("Votre proposition? ").split()))
            proposition = [i for i in proposition if 1 <= i <= 6]
            if len(proposition) == 4:
                break
            print("Oops! Il y a eu une erreur.")

        except (ValueError, NameError):
            print("Oops! Il y a eu une erreur.")

    return proposition


print("Pouvez-vous trouver ma combinaison de 4 symboles")
print("[chiffres entre 1 et 6 avec repetitions possibles]")
print("en moins de 10 coups? Entrez les symboles des")
print("propositions terminees par [Entree].")
print("(# un bien place, o un mal place)")


combinaison = [randint(1, 6) for _ in range(4)]
combinaison = [5, 2, 1, 2]
proposition = [0, 0, 0, 0]
coup = 10

while proposition != combinaison and coup > 0:
    proposition = proposition_joueur()
    coup -= 1

    chaine = ""
    utilisés = []
    for i in range(len(proposition)):
        if proposition[i] == combinaison[i]:
            chaine += "# "
            utilisés.append(proposition[i])

    for i in proposition:
        if i in combinaison and i not in utilisés:
            chaine += "o "
            utilisés.append(i)

    chaine = list(map(chr, sorted(list(map(ord, chaine.split())))))
    print("".join(chaine) + f" (reste {coup} coups)")


if coup > 0:
    print(f"Bravo! Vous avez trouvé en {10-coup} coups")
else:
    print("Vous avez perdu!")

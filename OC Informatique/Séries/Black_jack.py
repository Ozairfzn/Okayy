from random import choice


jeu, joueur, banque = True, True, True
cartes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
mise = int(input("Combien misez-vous?  "))

Joueur, Banque = [], []
Joueur.append(choice(cartes))
Banque.append(choice(cartes))
print(f"Vos points: {Joueur[0]}\nLes points du croupier: {Banque[0]}")


while jeu:
    tour = 0

    while tour % 2 == 0:
        tour += 1

        if Banque:
            sommeB = 0
            for i in Banque:
                sommeB += i
            if sommeB > 21:
                jeu = False
            if sommeB > 16:
                banque = False
                break
            Banque.append(choice(cartes))
            sommeB = 0
            for i in Banque:
                sommeB += i

    while tour % 2 == 1:
        tour += 1

        if joueur:
            stop = input("Voulez-vous continuer? [oui]/non ")
            if stop == "non":
                joueur = False
                break
            Joueur.append(choice(cartes))

            sommeJ = 0
            for i in Joueur:
                sommeJ += i
            if sommeJ > 21:
                jeu = False

    print(f"Vos points: {sommeJ}")
    print(f"Les points du croupier: {sommeB}")

    if not banque and not joueur:
        jeu = False


if sommeB > 21:
    print("Vous avez doublé votre mise! ", 2*mise, "CHF")
elif sommeJ > 21:
    print("Vous avez perdu votre mise!")
else:
    if sommeB >= sommeJ:
        print("Vous avez perdu votre mise!")
    else:
        print("Vous avez doublé votre mise! ", 2*mise, "CHF")

# Exercice 4.1
n = int(input("Donnez une année"))

if n % 400 == 0:
    print("Cette année est bissextile")
elif n % 4 == 0 and n % 100 == 0:
    print("Cette année n'est pas bissextile")
elif n % 4 == 0:
    print("Cette année est bissextile")
else:
    print("Cette année n'est pas bissextile")

# Exercice 4.2
n = 51
while n < 150:
    print(n)
    n = n + 2

# Exercice 4.3
n = 1
while n <= 20:
    print(n, "* 7 =", 7*n)
    n += 1

# Exercice 4.4
n = 0
S = 0
while n < 1000:
    n = n + 1
    S = S + n
print(S)

# Execice 4.5
n = 1
while n <= 20:
    if (7*n) % 3 == 0:
        print(7*n, "*")
    else:
        print(7*n)
    n += 1

# Exercice 4.6
S = eval(input("Entrez un capital: "))
t = eval(input("Entrez un taux d'intérêt: "))
a = 0

while S < 1000:
    S = S + t * S
    a = a + 1

print("Le capital sera doublé après", a, "ans")

# Exercice 4.8
n = 0

while n <= 7:
    n += 1
    print(n * "*")

# Exercice 4.9
a = int(input("Entrez la borne inférieure: "))
b = int(input("Entrez la borne supérieure: "))

s = 0
while a <= b:
    if a % 15 == 0:
        s = s + a
    a = a + 1

print(s)

# 2)
a = int(input("Entrez la borne inférieure: "))
b = int(input("Entrez la borne supérieure: "))

s = 0
while a <= b:
    if a % 5 == 0 or a % 3 == 0:
        s = s + a
    a = a + 1

print(s)

# Exercice 4.10
n = 0
while n < 100:
    print("Je dois écrire 100 fois un texte inutile.")
    n += 1


# Exercice 4.11
nom1 = input("Quel est le nom du joueur 1 ? ")
nom2 = input("Quel est le nom du joueur 2 ? ")
n = 30
tour = 0
while n > 0:
    print(f"Information : Il reste {n} allumettes.")
    if tour % 2 == 0:
        enleve = int(input(f"Combien enlèves-tu d'allumettes {nom1} ? "))
        while enleve not in [1, 2, 3]:
            print("Tu ne peux que enlever 1, 2 ou 3 allumettes !")
            enleve = int(input(f"Combien enlèves-tu d'allumettes {nom1} ? "))
    else:
        enleve = int(input(f"Combien enlèves-tu d'allumettes {nom2} ? "))
        while enleve not in [1, 2, 3]:
            print("Tu ne peux que enlever 1, 2 ou 3 allumettes !")
            enleve = int(input(f"Combien enlèves-tu d'allumettes {nom2} ? "))
    n -= enleve
    tour += 1

if tour % 2 == 0:
    print(f"{nom1} a gagné(e)")
else:
    print(f"{nom2} a gagné(e)")

# Exercice 4.12
ligne = "\n----------------------------------------------"
nom1 = input("Quel est le nom du joueur ? ")
nom2 = "IA"
n = 30
tour = 0
while n > 0:
    print(f"Information : Il reste {n} allumettes.{ligne}")
    if tour % 2 == 0:
        enleve = int(input(f"Combien enlèves-tu d'allumettes {nom1} ? "))
        while enleve not in [1, 2, 3]:
            print("Tu ne peux que enlever 1, 2 ou 3 allumettes !")
            enleve = int(input(f"Combien enlèves-tu d'allumettes {nom1} ? "))
    else:
        if (n-1) % 4 == 0:
            enleve = 1
        else:
            enleve = (n-1) % 4
        print("L'IA a enlevée ", enleve)
    n -= enleve
    tour += 1

if tour % 2 == 0:
    print(f"{nom1} a gagné(e)")
else:
    print(f"{nom2} a gagné(e)")


# Exercice 4.13
fraction_piste_a_parcourir = 1
vitesse_tortue = 1
vitesse_piste = 10
jours = 0

while fraction_piste_a_parcourir > 0:
    fraction_piste_a_parcourir -= vitesse_tortue/(10 + jours*vitesse_piste)
    jours += 1
print(jours)

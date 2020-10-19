# Exercice 3.1
diviseur = eval(input("Entrez le diviseur: "))
dividant = eval(input("Entrez le dividant: "))

print(
    f"Le quotient de la division de {dividant} par {diviseur} faut {dividant//diviseur}.\nLe reste de la division de {dividant} par {diviseur} faut {dividant%diviseur}.")

# Exercice 3.4
n1 = eval(input("Entrez un nombre: "))
n2 = eval(input("Entrez un nombre: "))

if n1 > n2:
    print(f"{n1} est plus grand que {n2}.")
else:
    print(f"{n2} est plus grand que {n1}.")

# Exercice 3.5
DIVISEUR = 13
a = int(input("Entrez un nombre entier positif : "))
b = a/DIVISEUR
c = a//DIVISEUR
if b == c:
    print(f"{a} est un multiple de 13.")
else:
    print(f"{a} n'est pas un multiple de 13.")

    # Exercice 3.6
n36 = eval(input("Entrez un nombre: "))
print(n36 % 13 == 0)

# Exercice 3.8
chf = eval(input("Le montant total des achats: "))

if chf < 75:
    print(f"Il faut payer {75-(75*0.05)}CHF.")
else:
    print(f"Il faut payer {chf-(chf*0.08)}CHF.")

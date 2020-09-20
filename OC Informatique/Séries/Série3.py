# Exercice 3.1
diviseur = eval(input("Entrez le diviseur: "))
dividant = eval(input("Entrez le dividant: "))

print(f"Le quotient de la division de {dividant} par {diviseur} faut {dividant//diviseur}.\nLe reste de la division de {dividant} par {diviseur} faut {dividant%diviseur}.")

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
if b == c :
 print(f"{a} est un multiple de 13.")
else:
 print(f"{a} n'est pas un multiple de 13.")

 # Exercice 3.6
n36 = eval(input("Entrez un nombre: "))
print(n36 % 13 == 0)

# Exercice 3.7
import math

a = eval(input("Entrez le coefficient a de ax^2 + bx + c: "))
b = eval(input("Entrez le coefficient b de ax^2 + bx + c: "))
c = eval(input("Entrez le coefficient c de ax^2 + bx + c: "))

Delta = b**2 - 4*a*c

if Delta < 0:
    print(f"La fonction {a}x^2 + ({b}x) + ({c}) n'a pas de solution")
elif Delta == 0:
  print(f"La solution de la fonction {a}x^2 + ({b}x) + ({c}) est {-b/(2*a)}")
else:
    print(f"Les solutions de la fonction {a}x^2 + ({b}x) + ({c}) sont {(-b-math.sqrt(Delta))/(2*a)} et {(-b+math.sqrt(Delta))/(2*a)}")

# Exercice 3.8
chf = eval(input("Le montant total des achats: "))

if chf < 75:
    print(f"Il faut payer {75-(75*0.05)}CHF.")
else:
    print(f"Il faut payer {75-(75*0.08)}CHF.")
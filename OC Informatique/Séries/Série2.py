# Exercice 1.6
hauteur = 40
base = 62

aire = hauteur * base
print(f"L'aire du trapèze vaut {aire}")

PI = 3.14
rayon = 10
aire_disque = 2*PI * rayon**2
print(f"L'aire du disque vaut {aire_disque}")

# Exercice 1.7
#4
x = 7
#2
y = 2 * x
#1
y = y - 1
#4
x = x + 3 * y

# Exercice 1.8
somme = 1000
interet = 0.1
années = 3

somme_finale = somme * (1 + interet)**années
print(f"La somme finale après {années} ans vaut {round(somme_finale)}")

# Exercice 1.9
n = int(input("Entrez un nombre: "))
d = int(input("Entrez un nombre par le quel on divisera le premier: "))
q = n // d
r = n % d
print(f"{n} = {d} * {q} + {r}")


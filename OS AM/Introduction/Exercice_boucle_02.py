n = int(input("Entrez un nombre entier: "))

chaine = f"2^0"
somme = 1

for terme in range(1, n+1):
    chaine += f" + 2^{terme}"
    somme += 2**terme

print(f"La somme de {chaine} = {somme}")

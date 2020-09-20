h = eval(input("Entrez l'hauteur de la pièce: "))
l = eval(input("Entrez l'longueur de la pièce: "))
p = eval(input("Entrez l'profondeur de la pièce: "))
S = 2*h*(l+p)
n = S // 2.5
print(f"Il vous faut {int(n)} pots de peinture")

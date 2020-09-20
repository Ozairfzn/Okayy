a = eval(input("Entrez le coefficient a de ax + b: "))
b = eval(input("Entrez le coefficient b de ax + b: "))

if a != 0:
    print(f"Le zéro est à {-b/a}")
elif b == 0:
    print("Il y a une infinité de zéros")
else:
    print((f"Le zéro est à {b}"))

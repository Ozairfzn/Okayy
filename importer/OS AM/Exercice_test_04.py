a = eval(input("Entrez le coefficient a de ax + b: "))
b = eval(input("Entrez le coefficient b de ax + b: "))

if a != 0:
    print(f"Le zéro est à (0, {-b/a})")
else:
    print((f"Le zéro est à (0, {b})"))
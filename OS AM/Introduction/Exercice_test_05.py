import math

carre = chr(0x00B2)

a = eval(input(f"Entrez le coefficient a de ax{carre} + bx + c: "))
b = eval(input(f"Entrez le coefficient b de ax{carre} + bx + c: "))
c = eval(input(f"Entrez le coefficient c de ax{carre} + bx + c: "))

if a == 0 and b == 0 and c == 0:
    print(f"La fonction {a}x{carre} + ({b}x) + ({c}) à une infinté de zéros")
elif a == 0 and b == 0:
    print(f"Le zéro de la fonction {a}x{carre} + ({b}x) + ({c})  est {c}")
elif a == 0:
    print(f"Le zéro de la fonction {a}x{carre} + ({b}x) + ({c})  est {-c/b}")
else:
    Delta = b**2 - 4*a*c

    if Delta < 0:
        print(f"La fonction {a}x{carre} + ({b}x) + ({c})  n'a pas de zéro")
    elif Delta == 0:
        print(
            f"Le zéro de la fonction {a}x{carre} + ({b}x) + ({c})  est {-b/(2*a)}")
    else:
        print(
            f"Les zéros de la fonction {a}x{carre} + ({b}x) + ({c}) sont {(-b-math.sqrt(Delta))/(2*a)} et {(-b+math.sqrt(Delta))/(2*a)}")

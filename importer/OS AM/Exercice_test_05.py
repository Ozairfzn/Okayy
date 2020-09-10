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

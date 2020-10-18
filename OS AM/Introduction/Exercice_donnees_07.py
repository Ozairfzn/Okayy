# Partie a)

n = eval(input("Un entier à 2 chiffre: "))
x = str(n % 10)
y = str(n // 10)
p = int(x + y)
print(p)

# Partie b)

nb = eval(input("Un entier à 3 chiffre: "))
xb = str(nb % 10)
yb = str(nb // 10 % 10)
zb = str(nb // 100)
pb = int(xb + yb + zb)
print(pb)

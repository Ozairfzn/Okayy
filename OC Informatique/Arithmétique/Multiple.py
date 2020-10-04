Multiple = int(input("La somme des multiple de : "))
justqua = int(input("Borne supérieure : "))

n = justqua//Multiple

res = Multiple*(n*(n+1)/2)
print(int(res))
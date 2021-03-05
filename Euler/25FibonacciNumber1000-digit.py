a, b, i = 1, 1, 1
while len(str(a)) != 1000:
    a, b, i = b, a+b, i+1

print(i)
# 4782
for a in range(1, 1000):
    for b in range(a, 1000):
        for c in range(b, 1000):
            if a*a + b*b == c*c and a + b + c == 1000:
                print(a, b, c)


a, b, c = 200 ,375 ,425
print(a*a + b*b, c*c, a+b+c)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


def binome(k, n):
    if k == 0 or k == n:
        return 1
    return binome(k-1, n-1) + binome(k, n-1)


def pascal(nombre):
    for n in range(nombre):
        for k in range(n+1):
            print(binome(k, n), end="  ")
        print()


def pascalX(nombre):
    for n in range(nombre):
        for k in range(n+1):
            if binome(k, n) % 2 == 0:
                print(" ", end="")
            else:
                print("X", end="")
        print()

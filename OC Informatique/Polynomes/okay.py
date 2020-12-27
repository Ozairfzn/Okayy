i = -100
while True:
    try:
        print(1/10**i == float('inf'))
    except(ZeroDivisionError):
        print(i)
        break
    i -= 1

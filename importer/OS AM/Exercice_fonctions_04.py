def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a



def fibR(n):
    if n == 1 or n == 2:
        return 1
    return fibR(n-1) + fibR(n-2) 

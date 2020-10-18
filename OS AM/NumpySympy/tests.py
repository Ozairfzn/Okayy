from sympy import *


init_printing(use_latex=True)
x, y = symbols("x y")

res = integrate((1/x), x)
pprint(res)

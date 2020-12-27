from sympy import *


init_printing(use_latex=True)
x, y = symbols("x y")

res = simplify(2*x**2*(x**17-1)*(x**(1/2))/(x**13))
pprint(res)

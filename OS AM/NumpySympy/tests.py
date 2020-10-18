from sympy import *


init_printing(use_latex=True)
x = symbols("x")


pprint(Integral(sqrt(1/x), x))
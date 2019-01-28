from sympy import Symbol , factor , expand, pprint, init_printing , simplify , SympifyError , solve

x = Symbol('x')
expr = x - 5 -7
print(solve(expr))




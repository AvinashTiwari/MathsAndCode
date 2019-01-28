from sympy import Symbol , factor , expand, pprint, init_printing , simplify , SympifyError , solve

x = Symbol('x')
expr = x**2 + 5*x + 4
print(solve(expr, dict=True))

expr = x**2 + x +1
print(solve(expr, dict=True))

s = Symbol('s')
u =  Symbol('u')
t =  Symbol('t')
a = Symbol('a')
expr = u*t + (1/2)*a*t*t - s
t_expr = solve(expr, t , dict=True)
pprint(t_expr)
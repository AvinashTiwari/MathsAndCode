from sympy import Symbol , factor , expand
x = Symbol('x')
y = Symbol('y')
expr = x**2 - y**2
print("factor = " , factor(expr))
factors = factor(expr)
print("expand = ", expand( factors))

expr= x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr)
print("New factors ", factors)
print("New expand",  expand(factors))

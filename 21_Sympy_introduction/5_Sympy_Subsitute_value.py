from sympy import Symbol , factor , expand, pprint, init_printing , simplify

x = Symbol('x')
y = Symbol('y')

expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1, y:2})
print("Response after sub " , res)

res = expr.subs({x:1-y})
print("Response New Sub ", res)

expr_subs = expr.subs({x:1-y})
print('Simplify the experssion ',simplify(expr_subs) )

from sympy import Symbol , factor , expand, pprint, init_printing , simplify , SympifyError , solve

#2x + y =6
#3x + 2y = 12

x =  Symbol('x')
y =  Symbol('y')
expr1 = 2*x + 3*y -6
expr2 = 3*x + 2*y - 12

print('2x + 3y = 6 value is ' , solve((expr1, expr2), dict=True))
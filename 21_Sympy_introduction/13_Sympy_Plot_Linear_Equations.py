from sympy import Symbol , factor , expand, pprint, init_printing , simplify , SympifyError , solve
from sympy.plotting import plot
x = Symbol('x')

p = plot((2*x +3) , (x,-5,5), title='A Line', xlabel='x', ylabel='2x+3', show=False)
p.save('line.png')
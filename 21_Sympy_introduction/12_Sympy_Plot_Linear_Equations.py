from sympy import Symbol , factor , expand, pprint, init_printing , simplify , SympifyError , solve
from sympy.plotting import plot
x = Symbol('x')
plot(2*x+3)

plot((2*x +3) , (x,-5,5))
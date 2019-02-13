import  math
import sympy
from sympy import Symbol , Limit, S, Derivative ,sympify , pprint, sin, Integral
from sympy.core.sympify import SympifyError

x = Symbol('x')
k =  Symbol('k')
print('Integral : {0}'.format(Integral(k*x,x)))
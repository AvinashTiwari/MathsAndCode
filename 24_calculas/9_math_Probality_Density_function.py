import  math
import sympy
from sympy import Symbol , Limit, S, Derivative ,sympify , pprint, sin, Integral,sqrt,exp,pi
from sympy.core.sympify import SympifyError

x = Symbol('x')
k =  Symbol('k')
p = exp(-(x - 10 )**2/2)/sqrt(2*pi)
print('Integral density {0} '.format(Integral(p, (x,11,12)).doit().evalf()))
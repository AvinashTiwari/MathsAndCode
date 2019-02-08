import  math
import sympy
from sympy import Symbol , Limit, S

x = Symbol('x')
print("Limit {0} ".format(Limit(1/x,x,S.Infinity)))
l = Limit(1/x,x,S.Infinity)
print("Limit {0} ".format(l.doit()))





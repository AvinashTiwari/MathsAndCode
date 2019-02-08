import  math
import sympy
from sympy import Symbol , Limit, S, Derivative

t = Symbol('t')
St = 5*t**2 + 2*t +8
print("St .{0}".format(St))
print(Derivative(St,t))
d = Derivative(St,t)
print(d.doit())
print(d.doit().subs({t:1}))

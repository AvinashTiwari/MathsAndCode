import  math
import sympy
from sympy import Symbol

print("Math Sin {0} ".format(math.sin(math.pi/2)))
print("sympy Sin {0} ".format(sympy.sin(math.pi/2)))
theta = Symbol('theta')
print("Sympy Theta {0}".format(sympy.sin(theta) + sympy.sin(theta)))





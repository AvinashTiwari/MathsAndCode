from sympy import FiniteSet, pi
from fractions import Fraction

s = FiniteSet(1,2,3,4,5,6)
a = FiniteSet(2,3,5)
b = FiniteSet(1,3,5)
e = a.union(b)
print("probailty Event A and Event B {0}",format(len(e) / len(s)))

e = a.intersect(b)
print("probailty Event A or Event B {0}",format(len(e) / len(s)))
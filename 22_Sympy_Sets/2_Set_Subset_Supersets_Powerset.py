from sympy import FiniteSet
from fractions import Fraction

s =  FiniteSet(1)
t = FiniteSet(1,2)
print("Is s is subset of t " ,s.is_subset(t))
print("Is t is subset of s " ,t.is_subset(s))

s = FiniteSet(1,2,3)
ps = s.powerset()
print("Power set ", ps)

s = FiniteSet(1,2,3)
t = FiniteSet(1,2,3)
print("Is s is proper subset ", s.is_proper_subset(t))
print("Is t is proper subset ", t.is_proper_subset(s))

s = FiniteSet(1,2,3)
t = FiniteSet(1,2,3, 4)
print("Is s is proper subset ", s.is_proper_subset(t))
print("Is t is proper subset ", t.is_proper_subset(s))
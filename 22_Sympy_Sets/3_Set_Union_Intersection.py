from sympy import FiniteSet
from fractions import Fraction

s =  FiniteSet(1,2,3)
t = FiniteSet(2,4,6)
print("Union " , s.union(t))

s =  FiniteSet(1,2)
t = FiniteSet(2,3)
print("intersect  " , s.intersect(t))


s =  FiniteSet(1,2)
t = FiniteSet(2,3)
u = FiniteSet(3,5,7)
print("Union " , s.union(t).union(u))


s = FiniteSet(1,2)
t = FiniteSet(2,3)
p = s*t
print("Cartesian ", p)

for elem in p:
    print("Cartesian ", elem)

s = FiniteSet(1,2)
p = s**3
print("carteisna ** ", p)

for elem in p:
    print("Cartesian ", elem)

from sympy import FiniteSet
from fractions import Fraction
s = FiniteSet(2,4,6)
print(s)

s = FiniteSet(1, 1.5, Fraction(1,5))
print(s)

s = FiniteSet(1,1.5,3)
print("Lenth of Set ", len(s))

members  = {1,2,3}
s = FiniteSet(*members)
print("Set from List or tuple",s)


members  = {1,2,3,2}
s = FiniteSet(*members)
print("Set with Repetition ",s)


s = FiniteSet(1,2,3)
for members in s:
    print("Loop  inside the set ",members)


s = FiniteSet(2,4,6)
t = FiniteSet(2,4,6)
print("Comaprning 2 sets ", s == t)
import  math
import sympy
from sympy import Symbol , Limit, S

n = Symbol('n')
print("Compound Interest {0}".format(Limit((1+1/n)**n,n,S.Infinity)))
print(Limit((1+1/n)**n,n,S.Infinity).doit())


p = Symbol('p',positive =True)
r = Symbol('r',positive =True)
t = Symbol('t',positive =True)
print("Compound Interest {0}".format(Limit(p*(1+r/n)**(n*t),n,S.Infinity)))
print(Limit(p*(1+r/n)**(n*t),n,S.Infinity))
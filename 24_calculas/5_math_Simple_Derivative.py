import  math
import sympy
from sympy import Symbol , Limit, S, Derivative ,sympify , pprint
from sympy.core.sympify import SympifyError

def derivative(f,var):
    var = Symbol(var)
    d = Derivative(f,var).doit()
    pprint(d)

if __name__ == '__main__':
    f = input('Enter a function : ')
    var = input('Enter the variable to differentiate with respect to: ')
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid Input')
    else:
        derivative(f,var)
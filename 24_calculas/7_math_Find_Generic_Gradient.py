import  math
import sympy
from sympy import Symbol , Limit, S, Derivative ,sympify , pprint, sin
from sympy.core.sympify import SympifyError

def grad_ascent(xo, f1x, x):
    epsilon = 1e-6
    step_size = 1e-4
    x_old = xo
    x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    while abs(x_old - x_new ) > epsilon:
        x_old = x_new
        x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()

    return x_new



if __name__ == '__main__':
  f = input('Enter a function is one variable: ')
  var  = input('Enter the variable to diff with respect to: ')
  varO = float(input('enter the inital value of teh variable: '))
  try:
      f = sympify(f)
  except SympifyError:
      print('Invalid function entered')
  else:
      var = Symbol(var)
      d = Derivative(f,var).doit()
      var_max = grad_ascent(varO,d,var)
      print('{0}:{1}'.format(var.name,var_max))
      print('Max value : {0} '.format(f.subs({var:var_max})))
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

def find_max_theta(R, theta):
    R1theta = Derivative(R, theta).doit()
    thetao= 1e-3
    theta_max = grad_ascent(thetao, R1theta,theta)
    return theta_max

if __name__ == '__main__':
    g = 9.8
    u =25
    theta = Symbol('theta')
    R = u**2*sin(2*theta)/g

    theta_max = find_max_theta(R, theta)
    print('Theta: {0}'.format(math.degrees(theta_max)))
    print('Maxium Range: {0} '.format(R.subs({theta:theta_max})))
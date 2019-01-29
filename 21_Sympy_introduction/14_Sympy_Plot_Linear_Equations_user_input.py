from sympy import Symbol , factor , expand, pprint, init_printing , simplify , SympifyError , solve
from sympy.plotting import plot

def plot_expression(expr):
    y = Symbol('y')
    solutions = solve(expr,y)
    expr_y = solutions[0]
    plot(expr_y)

if __name__ == '__main__':
    expr = input('enter your expression in terms of x and y :')
    try:
        expr = simplify(expr)
    except SympifyError:
        print('Please input valid input')
    else:
        plot_expression(expr)

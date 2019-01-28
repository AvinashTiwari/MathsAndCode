from sympy import Symbol , factor , expand, pprint, init_printing , simplify , SympifyError 


def product(expr1 , expr2):
    prod = expand(expr1*expr2)
    print(prod)

if __name__ == '__main__':
    expr1 = input('Enter the first expression: ')
    expr2 = input('Enter the second expression: ')

    try:
        expr1 = simplify(expr1)
        expr2 = simplify(expr2)
    except SympifyError:
        print('Invalid input')
    else:
        product(expr1, expr2)

from fractions import Fraction

def add(a, b):
    print('Result of addition: {0}'.format(a + b))

if __name__ == '__main__':
    a = Fraction(input('Enter first fraction: '))
    b = Fraction(input('Enter first fraction: '))
    op = input('Operation to perform -add , subract , divide , multiply')
    if op == 'Add':
        add(a,b)
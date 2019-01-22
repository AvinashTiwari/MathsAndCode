import matplotlib.pyplot
from pylab import savefig ,plot , show
def create_graph():
    x_numbers = [1,2,3]
    y_numbers = [2,4,6]

    plot(x_numbers, y_numbers)
    savefig('1.png')
    show()
    

if __name__ == '__main__':
    create_graph()

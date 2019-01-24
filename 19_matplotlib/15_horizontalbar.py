
from pylab import savefig ,plot , show
import matplotlib.pyplot as plt
import math

def create_bar_chart(data , labels):
    number_bars = len(data)
    positions = range(1, number_bars + 1)
    plt.barh(positions, data, align='center')
    plt.yticks(positions, labels)
    plt.xlabel('Steps')
    plt.ylabel('Day')
    plt.title('Number of step walked')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    steps = [6534 , 7000, 8900, 10786, 3467, 11045, 5095]
    labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    create_bar_chart(steps,labels )

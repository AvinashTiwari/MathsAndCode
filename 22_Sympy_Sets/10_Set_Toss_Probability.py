from sympy import FiniteSet, pi
from fractions import Fraction

import matplotlib.pyplot as plt
import random


def toss():
    if random.random() < 2/3:
        return 0
    else:
        return 1

print("Toss value {0}".format(toss()))
from sympy import FiniteSet, pi
from fractions import Fraction

import matplotlib.pyplot as plt
import random

def find_prob(traget_score,maxrolls):
    die_slides = FiniteSet(1,2,3,4,5,6)
    s = die_slides**maxrolls
    if max_rolls >1:
        sucess_rolls = []
        for elem in s:
            if sum(elem) >= traget_score:
                sucess_rolls.append(elem)
    else:
        if traget_score >6:
            sucess_rolls = []
            for roll in die_slides:
                if roll >=traget_score:
                    sucess_rolls.append(roll)
    e =  FiniteSet(*sucess_rolls)
    return len(e) / len(s)

if __name__ == '__main__':
    target_score = int(input('enter the traget score:  '))
    max_rolls = int(input('enter Maxium number of rolls allowed: '))
    p = find_prob(target_score, max_rolls)
    print("Probabilty : {0:.5f}".format(p))
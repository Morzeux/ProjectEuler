# -*- coding: utf-8 -*-
'''
Created on 17.5.2014

@author: Morzeux
'''

POUNDS = [200, 100, 50, 20, 10, 5, 2]

def get_sum(num, arr, counter):
    """ Counts all possible sums. """
    val = -arr.pop(0)
    for i in [i for i in range(num, 0, val)] + [0]:
        if i != 0 or i == 0 and num % val == 0:
            if arr:
                get_sum(i, arr[:], counter)
            else:
                counter.append(1)

def problem(libres=2):
    """
    In England the currency is made up of pound, £, and pence, p, and there
    are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
    """

    count = int(libres * 100)
    counter = []
    get_sum(count, POUNDS[:], counter)

    return len(counter)

'''
Created on 14.5.2014

@author: Morzeux
'''

import math

def _try_triple(fst, sec):
    """ Evaluated triple. """
    res = math.sqrt(math.pow(fst, 2) + math.pow(sec, 2))

    if math.fabs(res - int(res)) != 0 or sec >= int(res):
        return None
    else:
        return int(res)

def problem(num=1000):
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c,
    for which,

    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    fst = 2
    sec = 3
    while True:
        trd = _try_triple(fst, sec)
        if trd and (fst + sec + trd) == num:
            break
        elif sec >= num / 2 or trd and (fst + sec + trd) > num:
            fst += 1
            sec = fst + 1
        elif fst >= num / 3:
            return None
        else:
            sec += 1

    return fst * sec * trd

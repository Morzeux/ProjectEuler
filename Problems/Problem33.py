'''
Created on 17.5.2014

@author: Morzeux
'''

import functools

def evaluate(fst, sec):
    """ Evaluates if curious fraction. """
    if fst == sec:
        return False
    res = fst / float(sec)
    fst = str(fst)
    sec = str(sec)
    if res and fst[-1] == sec[0]:
        fst = int(fst[0])
        sec = int(sec[-1])
        if sec > 0 and res == fst / float(sec):
            return True

    return False

def max_div(fst, sec):
    """ Find highest common division. """
    values = sorted([fst, sec])
    division = 1
    for i in range(2, values[0] + 1):
        if values[0] % i == 0 and values[1] % i == 0:
            division = i

    return division

def problem(num=2):
    """
    The fraction 49/98 is a curious fraction, as an inexperienced mathematician
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
    which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and
    denominator.

    If the product of these four fractions is given in its lowest common terms,
    find the value of the denominator.
    """
    max_v = int('9' * num) + 1
    min_v = int(max_v / 10)

    solutions = []
    for i in range(min_v, max_v):
        for j in range(min_v, max_v):
            if evaluate(i, j):
                solutions.append((i, j))

    num = functools.reduce(lambda x, y: x * y[0], solutions, 1)
    den = functools.reduce(lambda x, y: x * y[1], solutions, 1)

    return den / max_div(num, den)

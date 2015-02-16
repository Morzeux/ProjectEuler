# -*- coding: utf-8 -*-
'''
Created on 12.7.2014

@author: Morzeux
'''
import math

def fraction_number(num):
    """ Returns fraction number of requested square. """
    m_val = 0
    d_val = 1
    a_val = int(math.sqrt(num))
    while True:
        if math.sqrt(num) == int(math.sqrt(num)):
            yield (0, 0, 0)
        else:
            yield (m_val, d_val, a_val)
            m_val = d_val * a_val - m_val
            d_val = (num - m_val**2) / d_val
            a_val = int((math.sqrt(num) + m_val) / d_val)

def find_period(num):
    """ Finds fraction period of specified number. """
    frac_gen = fraction_number(num)
    next(frac_gen)
    counter = 1
    old_triple = next(frac_gen)
    while True:
        new_triple = next(frac_gen)
        if old_triple == new_triple:
            return counter
        else:
            counter += 1

def problem(max_num=10000):
    """
    All square roots are periodic when written as continued fractions and can
    be written in the form:

        √N = a0 + (1 / (a1 + 1 / (a2 + 1 / (a3 + ...))))

    For example, let us consider √23:

        √23 = 4 + √23 — 4 = 4 + 1 / (1 / √23—4) = 4 + (1 / (1 + (√23 – 3) / 7))

    If we continue we would get the following expansion:

        √23 = 4 + 1 / (1 + 1 / (3 + 1 / (1 + (1 / 8 + ...))))

    The process can be summarised as follows:

        a0 = 4, 1 / (√23 — 4) = (√23 + 4) / 7 = (√23 — 3) / 7
        a1 = 1, 7 / (√23 — 3) = 7 * (√23 + 3) / 14 = 3 + (√23 — 3) / 2
        a2 = 3, 2 / (√23 — 3) = 2 * (√23 + 3) / 14 = 1 + (√23 — 4) / 7
        a3 = 1, 7 / (√23 — 4) = 7 * (√23 + 4) / 7 = 8 + √23 — 4
        a4 = 8, 1 / (√23 — 4) = (√23 + 4) / 7 = 1 + (√23 — 3) / 7
        a5 = 1, 7 / (√23 — 3) = 7 * (√23 + 3) / 14 = 3 + (√23 — 3) / 2
        a6 = 3, 2 / (√23 — 3) = 2 * (√23 + 3) / 14 = 1 + (√23 — 4) / 7
        a7 = 1, 7 / (√23 — 4) = 7 * (√23 + 4) / 7 = 8 + √23 — 4

    It can be seen that the sequence is repeating. For conciseness, we use the
    notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
    indefinitely.

    The first ten continued fraction representations of (irrational) square
    roots are:

        √2=[1;(2)], period=1
        √3=[1;(1,2)], period=2
        √5=[2;(4)], period=1
        √6=[2;(2,4)], period=2
        √7=[2;(1,1,1,4)], period=4
        √8=[2;(1,4)], period=2
        √10=[3;(6)], period=1
        √11=[3;(3,6)], period=2
        √12= [3;(2,6)], period=2
        √13=[3;(1,1,1,1,6)], period=5

    Exactly four continued fractions, for N ≤ 13, have an odd period.

    How many continued fractions for N ≤ 10000 have an odd period?
    """

    counter = 0
    for i in range(2, max_num + 1):
        if math.sqrt(i) != int(math.sqrt(i)) and find_period(i) % 2 == 1:
            counter += 1

    return counter

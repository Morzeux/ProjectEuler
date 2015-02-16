'''
Created on 17.5.2014

@author: Morzeux
'''

def find_chain(num):
    """ Finds chain of number. """
    evl = 1
    i = 0
    chain = {}
    while not chain.get(evl):
        chain[evl] = i
        evl = evl * 10 % num
        i += 1

    return i - chain[evl]

def problem(num=1000):
    """
    A unit fraction contains 1 in the numerator. The decimal representation
    of the unit fractions with denominators 2 to 10 are given:

        1/2     =     0.5
        1/3     =     0.(3)
        1/4     =     0.25
        1/5     =     0.2
        1/6     =     0.1(6)
        1/7     =     0.(142857)
        1/8     =     0.125
        1/9     =     0.(1)
        1/10    =     0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
    It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.
    """

    values = [(i, find_chain(i)) for i in range(1, num)]
    maximum = values[0]
    for value in values:
        if value[1] > maximum[1]:
            maximum = value

    return maximum[0]

'''
Created on 15.5.2014

@author: Morzeux
'''

import functools

def get_factorial(num):
    """ Returns factorial number. """
    return functools.reduce(lambda y, z: y * z, range(1, num + 1), 1)

def problem(edge=20):
    """
    Starting in the top left corner of a 2x2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right
    corner.

    How many such routes are there through a 20x20 grid?
    """
    return get_factorial(2*edge) / (get_factorial(edge) * get_factorial(edge))

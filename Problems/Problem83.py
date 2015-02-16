'''
Created on 17.5.2014

@author: Morzeux
'''

from Problems import Problem81

def problem(demo=False):
    """
    NOTE: This problem is a significantly more challenging version of
    Problem 81.

    In the 5 by 5 matrix below, the minimal path sum from the top left to the
    bottom right, by moving left, right, up, and down, is indicated in bold red
    and is equal to 2297.

        131    673    234    103     18
        201     96    342    965    150
        630    803    746    422    111
        537    699    497    121    956
        805    732    524     37    331

    Find the minimal path sum, in matrix.txt (right click and
    'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix,
    from the top left to the bottom right by moving left, right, up, and down.
    """
    return Problem81.solve(['left', 'right', 'ups', 'down'], demo)

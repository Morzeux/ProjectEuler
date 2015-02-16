'''
Created on 9.7.2014

@author: Morzeux
'''

def generate_cubes(max_num):
    """ Generator for cubic numbers. """
    i = 1
    while i < max_num:
        yield i**3
        i += 1

def problem(perms=5):
    """
    The cube, 41063625 (345^3), can be permuted to produce two other cubes:
    56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
    cube which has exactly three permutations of its digits which are also
    cube.

    Find the smallest cube for which exactly five permutations of its digits
    are cube.
    """

    generator = generate_cubes(float("inf"))
    solutions = {}
    while True:
        val = next(generator)
        s_val = "".join([str(i) for i in sorted([int(i) for i in str(val)])])
        if s_val not in solutions:
            solutions[s_val] = []

        solutions[s_val].append(val)
        if len(solutions[s_val]) == perms:
            return min(solutions[s_val])

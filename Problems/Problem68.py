'''
Created on 17.5.2014

@author: Morzeux
'''

from itertools import permutations

def _convert_triple(triple):
    """ Converts triple to string values. """
    return [str(val) for val in triple]

def _sum_vals(values):
    """ Sums three string integer values. """
    return sum([int(val) for val in values])

def _evaluate(extern, intern, arr):
    """ Finds magic triple and append it to array. """
    interns = []
    extern = [int(val) for val in extern]
    min_item = min(extern)
    extern.remove(min_item)
    extern = [str(val) for val in [min_item] + extern]

    for _ in range(len(intern)):
        interns.append(intern)
        intern = [intern[-1]] + intern[:-1]

    sums = []
    for intern in interns:
        for idx, _ in enumerate(intern):
            sums.append([
                extern[idx],
                intern[idx],
                intern[(idx + 1) % len(intern)]
            ])

        if len(set([_sum_vals(sum_value) for sum_value in sums])) == 1:
            magic = ([''.join(val) for val in sums])
            arr.append(''.join(magic))

def problem(gon=5, max_digit=16):
    """
    Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
    and each line adding to nine.

        https://projecteuler.net/project/images/p068_1.gif

    Working clockwise, and starting from the group of three with the
    numerically lowest external node (4,3,2 in this example), each solution can
    be described uniquely. For example, the above solution can be described by
    the set: 4,3,2; 6,2,1; 5,1,3.

    It is possible to complete the ring with four different totals: 9, 10, 11,
    and 12. There are eight solutions in total.

        Total    Solution Set
         9    4,2,3; 5,3,1; 6,1,2
         9    4,3,2; 6,2,1; 5,1,3
        10    2,3,5; 4,5,1; 6,1,3
        10    2,5,3; 6,3,1; 4,1,5
        11    1,4,6; 3,6,2; 5,2,4
        11    1,6,4; 5,4,2; 3,2,6
        12    1,5,6; 2,6,4; 3,4,5
        12    1,6,5; 3,5,4; 2,4,6

    By concatenating each group it is possible to form 9-digit strings; the
    maximum string for a 3-gon ring is 432621513.

    Using the numbers 1 to 10, and depending on arrangements, it is possible
    to form 16- and 17-digit strings. What is the maximum 16-digit string
    for a "magic" 5-gon ring?

        https://projecteuler.net/project/images/p068_2.gif
    """

    extern_nodes = permutations(range(1, 2 * gon + 1), gon)

    arr = []
    for extern in extern_nodes:
        interns = [val for val in range(1, 2 * gon + 1) if val not in extern]
        for intern in permutations(interns):
            if len(set(extern + intern)) == len(extern + intern):
                _evaluate(
                    _convert_triple(extern),
                    _convert_triple(intern),
                    arr
                )

    arr = [int(val) for val in arr if len(val) <= max_digit]
    return max(arr)

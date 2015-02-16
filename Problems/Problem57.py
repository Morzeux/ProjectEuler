'''
Created on 22.5.2014

@author: Morzeux
'''

def problem(max_count=1000):
    """
    It is possible to show that the square root of two can be expressed
    as an infinite continued fraction.

        sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

    By expanding this for the first four iterations, we get:

        1 + 1/2 = 3/2 = 1.5
        1 + 1/(2 + 1/2) = 7/5 = 1.4
        1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
        1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

    The next three expansions are 99/70, 239/169, and 577/408, but the eighth
    expansion, 1393/985, is the first example where the number of digits in the
    numerator exceeds the number of digits in the denominator.

    In the first one-thousand expansions, how many fractions contain a
    numerator with more digits than denominator?
    """

    expr = (3, 2)
    count = 0
    for _ in range(1, max_count + 1):
        expr = (expr[0] + 2 * expr[1], expr[0] + expr[1])
        if len(str(expr[0])) > len(str(expr[1])):
            count += 1

    return count

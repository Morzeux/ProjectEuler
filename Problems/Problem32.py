'''
Created on 17.5.2014

@author: Morzeux
'''

def get_limit(num):
    """ Returns max digit value. """
    return int('9' * int(num / 2)) + 1

def evaluate(fst, sec, num, solutions):
    """ Evaluates if correct. """
    res = fst * sec
    if res not in solutions:
        eval_string = '%d%d%d' % (fst, sec, res)
        for i in range(1, num + 1):
            if len(eval_string) != num or str(i) not in eval_string:
                return False

        solutions.add(res)
        return True
    else:
        return False

def problem(num=9):
    """
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234,
    is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only
    include it once in your sum.
    """
    solutions = set([])

    for i in range(1, get_limit(num)):
        j = 1
        while len('%d%d' % (i, j)) < int(num * 0.7):
            evaluate(i, j, num, solutions)
            j += 1

    return sum(list(solutions))

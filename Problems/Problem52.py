'''
Created on 21.5.2014

@author: Morzeux
'''

def evaluate(count, num):
    """ Evaluates if correct. """
    if len(count) != len(num):
        return False

    for i in count:
        if i not in num:
            return False

    return True

def problem(num=6, digits=4):
    """
    It can be seen that the number, 125874, and its double, 251748, contain
    exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.
    """

    max_v = 10**digits
    min_v = 10**(digits - 1)

    for i in range(min_v, int(max_v / 5)):
        if len(set(str(i))) == len(str(i)):
            for j in range(2, num + 1):
                if not evaluate(str(i), str(i * j)):
                    break
            else:
                return i

    return problem(num, digits + 1)

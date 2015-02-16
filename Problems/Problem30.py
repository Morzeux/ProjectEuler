'''
Created on 17.5.2014

@author: Morzeux
'''

def digits_sum(num, pwd):
    """ Returns sum of powered digits. """
    return sum([int(i)**pwd for i in str(num)])

def problem(num=5):
    """
    Surprisingly there are only three numbers that can be written as the sum
    of fourth powers of their digits:

        1634 = 1^4 + 6^4 + 3^4 + 4^4
        8208 = 8^4 + 2^4 + 0^4 + 8^4
        9474 = 9^4 + 4^4 + 7^4 + 4^4
        As 1 = 1^4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.
    """
    min_n = digits_sum(str(''.join(num * '1')), num)
    max_n = digits_sum(str(''.join(num * '9')), num) + 1

    return sum([i for i in range(min_n, max_n) if digits_sum(i, num) == i])

'''
Created on 22.5.2014

@author: Morzeux
'''

def problem(num=100, pwd=100):
    """
    A googol (10^100) is a massive number: one followed by one-hundred zeros;
    100^100 is almost unimaginably large: one followed by two-hundred zeros.
    Despite their size, the sum of the digits in each number is only 1.

    Considering natural numbers of the form, a^b, where a, b < 100, what
    is the maximum digital sum?
    """

    return max([sum([int(k) for k in str(i**j)]) \
                for i in range(1, num) for j in range(1, pwd)])

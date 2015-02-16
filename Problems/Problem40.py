'''
Created on 18.5.2014

@author: Morzeux
'''

import functools

def problem(num=1000000):
    """
    An irrational decimal fraction is created by concatenating the positive
    integers:

        0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If d_n represents the n^th digit of the fractional part, find the value
    of the following expression.

        d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000
    """
    values = [10**i for i in range(len(str(num)))]
    eval_value = values.pop(0)
    i = 1
    chain = []
    results = []
    while values:
        chain += [c for c in str(i)]
        if len(chain) >= eval_value:
            results.append(int(chain[eval_value-1]))
            eval_value = values.pop(0)
        i += 1

    return functools.reduce(lambda x, y: x * y, results, 1)

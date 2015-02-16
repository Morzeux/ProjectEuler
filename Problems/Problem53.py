'''
Created on 21.5.2014

@author: Morzeux
'''

def compute(fst, sec, fact):
    """ Computes values. """
    return fact[fst] / (fact[sec] * (fact[fst - sec]))

def problem(num=100):
    """
    There are exactly ten ways of selecting three from five, 12345:

        123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    In combinatorics, we use the notation, 5~C_3 = 10.

    In general,

    n~C_r = n! / r!(n-r)!,
    where r <= n, n! = n x (n-1) x ... x 3 x 2 x 1, and 0! = 1.

    It is not until n = 23, that a value exceeds one-million:
        23~C_10 = 1144066.

    How many, not necessarily distinct, values of  n~C_r,
    for 1 <= n <= 100, are greater than one-million?
    """
    fact = {0: 1}
    val = 1
    for i in range(1, num + 1):
        val *= i
        fact[i] = val

    results = []
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            res = compute(i, j, fact)
            if res > 1000000:
                results.append(res)

    return len(results)

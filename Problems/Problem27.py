'''
Created on 17.5.2014

@author: Morzeux
'''
import math

NON_PRIMES = set([])
PRIMES = set([])

def is_prime(num):
    """ Checks if prime. """
    num = int(math.fabs(num))
    if num not in NON_PRIMES and num not in PRIMES:
        for i in range(2, int(num / 2 + 1)):
            if num % i == 0:
                NON_PRIMES.add(num)
                return False

        PRIMES.add(num)
        return True
    elif num in PRIMES:
        return True
    elif num in NON_PRIMES:
        return False
    else:
        raise ValueError

def formula(fst, sec, num):
    """ Evaluation formula. """
    return num * num + fst * num + sec

def evaluate_formula(fst, sec):
    """ Evaluates two number according to formula. """
    if is_prime(fst) and is_prime(sec):
        num = 0
        res = None
        while num == 0 or is_prime(res):
            res = formula(fst, sec, num)
            num += 1

        return num - 2
    else:
        return 0

def problem(num=1000):
    """
    Euler discovered the remarkable quadratic formula:

        n^2 + n + 41

    It turns out that the formula will produce 40 primes for the consecutive
    values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
    is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
    divisible by 41.

    The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80
    primes for the consecutive values n = 0 to 79. The product of the
    coefficients, -79 and 1601, is -126479.

    Considering quadratics of the form:

        n^2 + an + b, where |a| < 1000 and |b| < 1000

        where |n| is the modulus/absolute value of n
        e.g. |11| = 11 and |-4| = 4

    Find the product of the coefficients, a and b, for the quadratic expression
    that produces the maximum number of primes for consecutive values of n,
    starting with n = 0.
    """
    result = (0, 0)
    for i in range(-num + 1, num):
        for j in range(-num + 1, num):
            res = evaluate_formula(i, j)
            if res > result[0]:
                result = (res, i * j)

    return result[1]

'''
Created on 17.5.2014

@author: Morzeux
'''

from Problems import Problem10

MAX = 1000000

def is_prime(num, maximum, primes):
    """ Checks if number is prime. """
    if num < maximum and num not in primes:
        return False
    elif num not in primes:
        for i in range(2, num / 2 + 1):
            if num % i == 0:
                return False

    return True

def is_truncated(num, primes, left=False):
    """ Checks if is truncatable. """
    if is_prime(num, MAX, primes):
        num = str(num)
        if len(num) == 1:
            return True
        else:
            return is_truncated(int(num[1:])
                                if left else int(num[:-1]), primes, left)
    else:
        return False

def evaluate(num, primes):
    """ Evaluates if number in truncatable. """
    if is_truncated(num, primes, True) and is_truncated(num, primes):
        return True
    else:
        return False

def problem():
    """
    The number 3797 has an interesting property. Being prime itself,
    it is possible to continuously remove digits from left to right,
    and remain prime at each stage: 3797, 797, 97, and 7. Similarly
    we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable
    from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    """
    primes = set(Problem10.generate_primes(MAX))
    evaluated = []
    i = 10
    while len(evaluated) < 11:
        if evaluate(i, primes):
            evaluated.append(i)
        i += 1

    return sum(evaluated)

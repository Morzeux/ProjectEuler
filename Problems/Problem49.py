'''
Created on 19.5.2014

@author: Morzeux
'''

from Problems import Problem10
import itertools

def evaluate(i, prime, set_primes):
    """"Evaluates if correct. """
    sec = prime + i
    thd = prime + 2 * i
    if sec in set_primes and thd in set_primes:
        perms = set(int(''.join(perm)) \
                    for perm in itertools.permutations(str(prime)))

        if sec in perms and thd in perms:
            return (prime, sec, thd)

    return False

def problem():
    """
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms
    are prime, and, (ii) each of the 4-digit numbers are permutations of one
    another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit
    increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this
    sequence?
    """
    primes = Problem10.generate_primes(10000)
    primes = [prime for prime in primes if prime >= 1000]
    set_primes = set(primes)
    results = []
    for prime in primes:
        for i in range(1, 4501): # maximal adder
            res = evaluate(i, prime, set_primes)
            if res:
                results.append(res)
    return int(''.join(str(num) for num in results[-1]))

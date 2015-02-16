'''
Created on 14.5.2014

@author: Morzeux
'''

def _problem(max_count, fin_prime):
    """ Helper function. """
    if not fin_prime:
        fin_prime = max_count

    primes = []
    arr = list(range(2, max_count * 10 + 1))

    def get_value(arr):
        """ One iteration of sieve. """
        primes.append(arr.pop(0))
        return [i for i in arr if not i % primes[-1] == 0]

    while arr and len(primes) < fin_prime:
        arr = get_value(arr)

    if len(primes) >= fin_prime:
        return primes
    else:
        return _problem(max_count * 2, fin_prime)

def problem(count=10001):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    """
    return _problem(count, count)[-1]

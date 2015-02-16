'''
Created on 14.5.2014

@author: Morzeux
'''

import math

def generate_primes(num):
    """ Prime number generator. """
    primes = []
    cnt = 2
    arr = []
    while cnt <= num:
        arr.append(cnt)
        cnt += 1

    def get_value(arr):
        """ Eratosten sieve. """
        primes.append(arr.pop(0))
        return [i for i in arr if not i % primes[-1] == 0]

    while True:
        arr = get_value(arr)
        if primes[-1] > math.sqrt(num - 1):
            break

    return primes + arr

def problem(num=2000000):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    return sum(generate_primes(num))

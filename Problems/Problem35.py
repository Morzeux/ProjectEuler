'''
Created on 17.5.2014

@author: Morzeux
'''

from Problems import Problem10

def generate_circle(num):
    """ Rotate value and returns all their permutation. """
    num = str(num)
    perm = []
    for _ in range(len(num)):
        num = num[1:] + num[0]
        perm.append(int(num))

    return perm

def problem(num=1000000):
    """
    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?
    """

    primes = set(Problem10.generate_primes(num))
    evaluated = []
    for number in primes:
        perm = generate_circle(number)
        for value in perm:
            if value not in primes:
                break
        else:
            evaluated += perm

    return len(set(evaluated))

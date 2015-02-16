'''
Created on 19.5.2014

@author: Morzeux
'''

from Problems import Problem10

def evaluate(part, num):
    """ Evaluates if correct. """
    while part:
        if len(part[0][1]) == num:
            evl = part.pop(0)
            if part and evl[0] + 1 != part[0][0]:
                return False
        else:
            return False

    return True

def split_numbers(num):
    """ Split number between its divisors. """
    primes = Problem10.generate_primes(num)
    numbers = [(i, []) for i in range(4, num + 1)]
    for prime in primes:
        for num in range(prime, len(numbers)):
            if prime != numbers[num][0] and numbers[num][0] % prime == 0:
                numbers[num][1].append(prime)

    return numbers

def problem(num=4, max_v=150000):
    """
    The first two consecutive numbers to have two distinct prime factors are:

        14 = 2 x 7
        15 = 3 x 5

    The first three consecutive numbers to have three distinct prime factors
    are:

        644 = 2^2 x 7 x 23
        645 = 3 x 5 x 43
        646 = 2 x 17 x 19.

    Find the first four consecutive integers to have four distinct prime
    factors. What is the first of these numbers?
    """
    numbers = split_numbers(max_v)
    for i, _ in enumerate(numbers[:-num]):
        if evaluate(numbers[i:i + num], num):
            return numbers[i][0]

    return None

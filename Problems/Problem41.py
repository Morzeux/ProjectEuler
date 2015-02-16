'''
Created on 18.5.2014

@author: Morzeux
'''

import itertools

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_prime(num):
    """ Checks if number is prime. """
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False

    return True

def is_pandigital(num):
    """ Checks if prime is pandigital. """
    num = str(num)
    for number in NUMBERS[:len(num)]:
        if number not in num:
            return False

    return True

def problem(num=9):
    """
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
    and is also prime.

    What is the largest n-digit pandigital prime that exists?
    """
    for i in range(num + 1, 0, -1):
        numbers = sorted([j for j in itertools.permutations(range(1, i))],
                         reverse=True)

        for number in numbers:
            number = int(''.join([str(i) for i in number]))
            if is_pandigital(number) and is_prime(number):
                return number

    return None

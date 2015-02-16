'''
Created on 22.5.2014

@author: Morzeux
'''

from random import randint

def compute_modulo(number, exponent, modulo):
    """ Fastest way how to compute modulo numbers. """
    if number > modulo:
        number = number % modulo

    res = 1
    while exponent > 0:
        if exponent % 2 != 0:
            res = (res * number) % modulo
        exponent = int(exponent / 2)
        number = (number**2) % modulo

    return res

def rabin_miller(num, num_k=10):
    """
    Rabin-Miller test for evaluating if number is prime.

    If number is not prime, then it returns False. If number is probably prime,
    then it returns True. K param is number of performed tests.
    """
    if num is 2:
        return True

    num_d = num - 1

    num_r = 0
    while num_d % 2 == 0:
        num_r += 1
        num_d = int(num_d / 2)

    for _ in range(num_k):
        num_a = randint(2, num - 1)
        for i in range(num_r):
            res = compute_modulo(num_a, 2**i * num_d, num)
            if res == num - 1 or (res == 1 and i == 0):
                break
        else:
            return False

    return True

def evaluate(values):
    """ Returns prime ratio. """
    res = [(spr['primes'], len(spr['values'])) for spr in values.values()]
    primes = sum([i for i, _ in res])
    total = sum([i for _, i in res]) + 1
    return (primes / float(total)) * 100

def problem(ratio=10.0):
    """
    Starting with 1 and spiralling anticlockwise in the following way,
    a square spiral with side length 7 is formed.

        37 36 35 34 33 32 31
        38 17 16 15 14 13 30
        39 18  5  4  3 12 29
        40 19  6  1  2 11 28
        41 20  7  8  9 10 27
        42 21 22 23 24 25 26
        43 44 45 46 47 48 49

    It is interesting to note that the odd squares lie along the bottom
    right diagonal, but what is more interesting is that 8 out of the 13
    numbers lying along both diagonals are prime; that is, a ratio of
    8/13 ~ 62%.

    If one complete new layer is wrapped around the spiral above, a square
    spiral with side length 9 will be formed. If this process is continued,
    what is the side length of the square spiral for which the ratio of primes
    along both diagonals first falls below 10%?
    """

    values = {}
    for i in range(1, 5):
        values[i] = {'primes': 0, 'values': []}

    i = 0
    while True:
        for j in range(2, 10, 2):
            if not values[j / 2]['values']:
                start = 1
            else:
                start = values[j / 2]['values'][-1]

            value = start + j + i * 8
            values[j / 2]['values'].append(value)
            if j != 8 and rabin_miller(value):
                values[j / 2]['primes'] += 1

        res = evaluate(values)
        if res < ratio:
            return (i + 1) * 2 + 1
        i += 1

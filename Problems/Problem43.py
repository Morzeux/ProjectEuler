'''
Created on 18.5.2014

@author: Morzeux
'''
import itertools

def evaluate(num):
    """ Evaluates if correct. """

    def divisible(sub, number):
        """Checks i divisible. """
        return int(sub) % number == 0

    divisibles = [2, 3, 5, 7, 11, 13, 17]
    i = 1
    while divisibles:
        if not divisible(num[i:i+3], divisibles.pop(0)):
            return False
        i += 1

    return True

def problem():
    """
    The number, 1406357289, is a 0 to 9 pandigital number because it is made
    up of each of the digits 0 to 9 in some order, but it also has a rather
    interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way,
    we note the following:

        d2d3d4=406 is divisible by 2
        d3d4d5=063 is divisible by 3
        d4d5d6=635 is divisible by 5
        d5d6d7=357 is divisible by 7
        d6d7d8=572 is divisible by 11
        d7d8d9=728 is divisible by 13
        d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
    """
    number = ''.join([str(i) for i in range(10)])
    acceptable = []
    for perm in itertools.permutations(number):
        perm = ''.join(perm)
        if evaluate(perm):
            acceptable.append(perm)

    return sum([int(i) for i in acceptable])

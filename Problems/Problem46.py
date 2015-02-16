'''
Created on 18.5.2014

@author: Morzeux
'''
from Problems import Problem10

def problem(num=1000):
    """
    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.

        9 = 7 + 2x1^2
        15 = 7 + 2x2^2
        21 = 3 + 2x3^2
        25 = 7 + 2x3^2
        27 = 19 + 2x2^2
        33 = 31 + 2x1^2

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?
    """
    primes = set(Problem10.generate_primes(num))
    squares = [2 * (i**2) for i in range(100)]
    numbers = [i for i in range(2, num + 1) if i not in primes and i % 2 != 0]

    sums = set([])
    for prime in primes:
        for p_sum in squares:
            sums.add(prime + p_sum)

    for i in numbers:
        if i not in sums:
            return i

    return problem(num * 10)

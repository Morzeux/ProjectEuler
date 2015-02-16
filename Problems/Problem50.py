'''
Created on 19.5.2014

@author: Morzeux
'''

import Problems.Problem10

def evaluate(result, set_primes):
    """
    Evaluates if correct sentence.
    """
    res = sum(result)
    while res not in set_primes:
        res -= result.pop()

    return result

def problem(num=1000000):
    """
    The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds to a prime
    below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a
    prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?
    """
    primes = Problems.Problem10.generate_primes(num)
    set_primes = set(primes)
    res = 0
    result = []
    while primes and primes[0] * len(result) < num:
        res = prime = primes.pop(0)
        temp_result = [prime]
        for prm in primes:
            if res < num:
                temp_result.append(prm)
                res += prm
            else:
                if len(evaluate(temp_result, set_primes)) > len(result):
                    result = temp_result

    return sum(result)

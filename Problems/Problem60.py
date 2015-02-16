'''
Created on 1.6.2014

@author: Morzeux
'''

from Problems import Problem10
from Problems import Problem58
import itertools

def is_prime(prime, primes):
    """ Checks if number is prime. """

    if prime in primes or Problem58.rabin_miller(prime):
        return True
    else:
        return False

def evaluate(fst, sec, primes):
    """ Evaluates if permutations are concate. """

    def single_eval(perm):
        """ Single evaluation of two primes. """
        if is_prime(int(''.join([str(i) for i in perm])), primes):
            return True
        else:
            return False
    for perm in itertools.permutations([fst, sec]):
        if not single_eval(perm):
            return False

    return True

def convert_primes(primes, set_primes):
    """ Converts primes into tree structure. """
    if len(primes) == 1:
        return {primes[0]: {}}
    elif len(primes) == 0:
        return {}

    new_primes = {}
    for i, prime in enumerate(primes):
        for prime2 in primes[i+1:]:
            if evaluate(prime, prime2, set_primes):
                if prime not in new_primes:
                    new_primes[prime] = []
                new_primes[prime].append(prime2)

    return new_primes

def find_concates(num, solutions, set_primes):
    """ Recursively searches for raw concates. """
    if num > 0:
        for key, values in solutions.items():
            if num > 1:
                values = convert_primes(values, set_primes)

            solutions[key] = find_concates(num - 1, values, set_primes)

    return solutions

def process_raw_concates(solutions, main_arr, pom_arr):
    """ Process raw concates into readable data. """
    if solutions and type(solutions) == dict:
        for key, value in solutions.items():
            process_raw_concates(value, main_arr, pom_arr[:] + [key])
    elif solutions and type(solutions) == list:
        for item in solutions:
            main_arr.append(pom_arr[:] + [item])
    else:
        main_arr.append(pom_arr[:])

def problem(num=5, max_primes=1000):
    """
    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
    primes and concatenating them in any order the result will always be prime.
    For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
    these four primes, 792, represents the lowest sum for a set of four primes
    with this property.

    Find the lowest sum for a set of five primes for which any two primes
    concatenate to produce another prime.
    """

    primes = Problem10.generate_primes(max_primes)
    set_primes = set(primes)

    arr = []
    solutions = find_concates(num - 1,
                              convert_primes(primes, set_primes),
                              set_primes)

    process_raw_concates(solutions, arr, [])
    result = [sum(i) for i in arr if len(i) == num]
    return min(result) if result else problem(num, max_primes * 10)

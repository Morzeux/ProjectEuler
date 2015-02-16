'''
Created on 19.5.2014

@author: Morzeux
'''

from Problems import Problem10

def get_bin(num, count):
    """ Returns binary string. """
    binary = str(bin(num))[2:]
    left = len(str(bin(2**count))[2:]) - len(binary) - 1
    return '%s%s' % (left * '0', binary)

def evaluate_bin(binary):
    """ Evaluates if correct binary number. """
    binary = str(binary)
    if binary[-1] != '1' and \
    len([char for char in binary if char == '1']) == 3:
        return True
    else:
        return False

def evaluate(prime, mask, primes):
    """ Evaluates if correct. """
    if prime[0] == '0':
        return []

    mask_value = -1
    for idx, value in enumerate(mask):
        if value == '1' and mask_value == -1 and prime[idx] in ['0', '1', '2']:
            mask_value = prime[idx]
        elif value == '1' and prime[idx] != mask_value:
            return []

    prime2 = ''
    for idx, value in enumerate(mask):
        if value == '1':
            prime2 += '%d'
        else:
            prime2 += prime[idx]

    count = [prime]
    for num in range(10):
        eval_prime = prime2 % (num, num, num)
        if prime != eval_prime and eval_prime in primes:
            count.append(eval_prime)
            continue

    return count

def problem(count=4, family=8):
    """
    By replacing the 1st digit of the 2-digit number *3, it turns out that six
    of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this
    5-digit number is the first example having seven primes among the ten
    generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
    56773, and 56993. Consequently 56003, being the first member of this
    family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number (not
    necessarily adjacent digits) with the same digit, is part of an eight
    prime value family.

    My Notes:
    ----------
    - all primes are not divisible by three, so three is a good candidate
    to exploit

    - last digit will not be replaced (primes ends only with 1, 3, 7 or 9)

    - for 4 digit number there is one possible mask
    - for 5 digit number there are 6 possible masks
    - for 6 digit number there are 10 possible masks
    """

    min_v = 10**(count-1)
    max_v = 10**count

    primes = Problem10.generate_primes(max_v)
    primes = [str(prime) for prime in primes if prime >= min_v]
    set_primes = set(primes)

    binaries = [get_bin(i, count) for i in range(1, 2**count)]
    binaries = [i for i in binaries if evaluate_bin(i)]

    for prime in primes:
        for mask in binaries:
            if len(evaluate(prime, mask, set_primes)) == family:
                return int(prime)

    return problem(count + 1, family)

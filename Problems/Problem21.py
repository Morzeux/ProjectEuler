'''
Created on 15.5.2014

@author: Morzeux
'''

def dels(num):
    """ Return deviations of number. """
    return [i for i in range(1, int(num / 2 + 1)) if num % i == 0]

def evaluate(num):
    """ Evaluates problem. """
    num2 = sum(dels(num))
    return True if num != num2 and sum(dels(num2)) == num else False

def problem(num=10000):
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n
    which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then a
    and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
    55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
    71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """
    numbers = []
    for i in range(1, num + 1):
        if evaluate(i):
            numbers.append(i)

    return sum(numbers)

'''
Created on 17.5.2014

@author: Morzeux
'''

def problem():
    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial
    of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """
    fact = {0: 1}
    num = 1
    for i in range(1, 10):
        num *= i
        fact[i] = num

    results = []
    i = 10
    while len(str(i)) <= len(str(fact[9])):
        if sum([fact[int(num)] for num in str(i)]) == i:
            results.append(i)
        i += 1

    return sum(results)

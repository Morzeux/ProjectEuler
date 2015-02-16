'''
Created on 14.5.2014

@author: Morzeux
'''

def problem(num=20):
    """
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20?
    """
    res = num
    while True:
        for i in reversed(range(1, num + 1)):
            if res % i != 0:
                res += num
                break
        else:
            return res

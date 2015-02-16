'''
Created on 19.5.2014

@author: Morzeux
'''

def problem(num=1000):
    """
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """
    return int(str(sum([i**i for i in range(1, num + 1)]))[-10:])

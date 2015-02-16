'''
Created on 14.5.2014

@author: Morzeux
'''

def divide(num):
    """ Find first divisor. """
    cnt = 2
    while cnt < num:
        if num % cnt == 0:
            return cnt
        cnt += 1

    return num

def split_number(cnt, arr):
    """ Splits number into its divisions. """
    div = divide(cnt)
    if div != cnt:
        arr.append(div)
        split_number(cnt / div, arr)
    else:
        arr.append(cnt)

def problem(cnt=600851475143):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """

    arr = []
    split_number(cnt, arr)
    return arr[-1]

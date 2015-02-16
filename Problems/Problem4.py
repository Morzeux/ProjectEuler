'''
Created on 14.5.2014

@author: Morzeux
'''

def problem(cnt=3):
    """
    A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    cnt = 10**cnt
    return max(a * b for a in range(cnt) for b in range(cnt)
               if str(a * b) == str(a * b)[::-1])

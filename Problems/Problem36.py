'''
Created on 17.5.2014

@author: Morzeux
'''

def is_palindrome(num):
    """ Checks if number is palindrome. """
    return True if str(num) == str(num)[::-1] else False

def problem(num=1000000):
    """
    The decimal number, 585 = 1001001001_2 (binary), is palindromic in both
    bases.

    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include
    leading zeros.)
    """
    return sum([i for i in range(1, num)\
                if is_palindrome(i) and is_palindrome(int(str(bin(i))[2:]))])

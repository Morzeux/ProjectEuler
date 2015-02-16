'''
Created on 18.5.2014

@author: Morzeux
'''

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_pandigit(num):
    """ Checks if is pandigit. """

    if len(num) == 9:
        for number in NUMBERS:
            if number not in num:
                return False

        return int(num)
    else:
        return False

def evaluate(num):
    """ Evaluates if correct. """
    evl = 0
    i = 1
    res = []
    while evl < 9:
        res.append(str(num * i))
        evl += len(res[-1])
        i += 1

    if i > 2:
        return is_pandigit(''.join(res))
    else:
        return False

def problem():
    """
    Take the number 192 and multiply it by each of 1, 2, and 3:

        192 x 1 = 192
        192 x 2 = 384
        192 x 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576.
    We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product
    of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2, ... , n) where n > 1?
    """
    maximum = 0
    for i in range(10000):
        res = evaluate(i)
        if res and res > maximum:
            maximum = res

    return maximum

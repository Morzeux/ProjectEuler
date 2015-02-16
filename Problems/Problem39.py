'''
Created on 18.5.2014

@author: Morzeux
'''
import math

def evaluate(fst, sec):
    """ Evaluates if correct. """
    res = math.sqrt(fst**2 + sec**2)
    return int(fst + sec + res) if math.fabs(res - int(res)) == 0 else False

def problem(num=1000):
    """
    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

        {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p <= 1000, is the number of solutions maximised?
    """
    numbers = {}

    for i in range(1, num + 1):
        for j in range(i, num + 1):
            res = evaluate(i, j)
            if res:
                if res not in numbers:
                    numbers[res] = [sorted((i, j))]
                else:
                    numbers[res].append(sorted((i, j)))

    numbers = sorted(numbers.items())
    converted = []
    for item in numbers:
        if item[0] <= num:
            converted.append((item[0], len(item[1])))
        else:
            break

    maximum = (0, 0)
    for item in converted:
        if item[1] > maximum[1]:
            maximum = item

    return maximum[0]

'''
Created on 11.7.2014

@author: Morzeux
'''

def problem():
    """
    The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
    number, 134217728=8^9, is a ninth power.

    How many n-digit positive integers exist which are also an nth power?
    """

    solutions = []

    for power in range(1, 1000):
        num = 1
        while True:
            res = num**power
            if len(str(res)) == power:
                solutions.append(res)
            elif len(str(res)) > power:
                break
            num += 1

    return len(solutions)

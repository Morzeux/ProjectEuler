'''
Created on 17.5.2014

@author: Morzeux
'''

def problem(num=1001):
    """
    Starting with the number 1 and moving to the right in a clockwise
    direction a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001
    spiral formed in the same way?
    """
    width = int(num / 2)
    sums = []
    for i in range(2, 10, 2):
        cnt = 1
        nums = []
        for j in range(width):
            cnt += (i + j * 8)
            nums.append(cnt)
        sums.append(sum(nums))

    return sum(sums) + 1

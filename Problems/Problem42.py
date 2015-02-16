'''
Created on 18.5.2014

@author: Morzeux
'''

import os

WORDS = os.path.join('Problems', 'words.txt')

def convert_word(word):
    """ Converts word to its integer value. """
    return sum([ord(i) - 96 for i in word])

def generate_triangle_number(num):
    """ Generates triangle number. """
    return int(0.5 * num * (num + 1))

def problem():
    """
    The nth term of the sequence of triangle numbers is given by,
    tn = (1/2) * n * (n + 1); so the first ten triangle numbers are:

        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value. For
    example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
    value is a triangle number then we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
    containing nearly two-thousand common English words, how many are triangle
    words?
    """
    with open(WORDS, 'r') as flr:
        words = flr.read()

    words = [word.strip()[1:-1].lower() for word in words.strip().split(',')]
    words = [convert_word(word) for word in words]
    maximum = max(words)
    triangle_numbers = []
    while not triangle_numbers or triangle_numbers[-1] < maximum:
        triangle_numbers.append(
            generate_triangle_number(len(triangle_numbers) + 1))

    triangle_numbers = set(triangle_numbers)
    return len([i for i in words if i in triangle_numbers])

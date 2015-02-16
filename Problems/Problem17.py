'''
Created on 15.5.2014

@author: Morzeux
'''

LETTERS = {0: '',
           1: 'one',
           2: 'two',
           3: 'three',
           4: 'four',
           5: 'five',
           6: 'six',
           7: 'seven',
           8: 'eight',
           9: 'nine',
           10: 'ten',
           11: 'eleven',
           12: 'twelve',
           13: 'thirteen',
           14: 'fourteen',
           15: 'fifteen',
           16: 'sixteen',
           17: 'seventeen',
           18: 'eighteen',
           19: 'nineteen',
           20: 'twenty',
           30: 'thirty',
           40: 'forty',
           50: 'fifty',
           60: 'sixty',
           70: 'seventy',
           80: 'eighty',
           90: 'ninety'}

def get_letters(num):
    """ Returns number written as word. """
    letters = LETTERS.get(num)
    num = str(num)
    if letters is not None:
        return letters
    elif len(num) == 2:
        return '%s-%s' % (
            LETTERS.get(int(num[0]) * 10), LETTERS.get(int(num[1])))

    elif len(num) == 3:
        second_part = get_letters(int(num[1:]))
        second_part = 'and %s' % second_part if second_part else ''
        return '%s hundred %s' % (get_letters(int(num[0])), second_part)
    elif num == '1000':
        return 'one thousand'
    else:
        return 'unknown'

def count_letters(word_num):
    """ Returns count of letters. """
    return len(word_num.replace('-', '').replace(' ', ''))

def problem(num=1000):
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance with
    British usage.
    """
    return sum([count_letters(get_letters(i)) for i in range(1, num + 1)])

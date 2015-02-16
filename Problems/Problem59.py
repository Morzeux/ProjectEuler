'''
Created on 31.5.2014

@author: Morzeux
'''
import os
import itertools

CIPHERS = os.path.join('Problems', 'cipher1.txt')

def to_bin(val):
    """ Transfers decimal string to binary string. """
    return bin(val)[2:]

def perform_xor(val, key):
    """ Performs XOR for value with provided key. """
    values = sorted([val, key])
    values = [to_bin(val) for val in values]
    diff = len(values[1]) - len(values[0])
    values[0] = '%s%s' % (diff * '0', values[0])

    xored = ''
    for i, val in enumerate(values[0]):
        if val != values[1][i]:
            xored += '1'
        else:
            xored += '0'

    return xored

def evaluate_xored(value):
    """ Evaluates if decripted value is ASCII value. """
    value = int(value, 2)
    if value in range(32, 127):
        return value
    else:
        return None

def generate_keys(min_v, max_v, numbers):
    """ Generates all combinations for keys. """
    rang = range(min_v, max_v + 1)
    comb = itertools.combinations_with_replacement(rang, numbers)
    perm = itertools.permutations(rang, numbers)
    return set(list(comb) + list(perm))

def problem():
    """
    Each character on a computer is assigned a unique code and the preferred
    standard is ASCII (American Standard Code for Information Interchange).
    For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

    A modern encryption method is to take a text file, convert the bytes to
    ASCII, then XOR each byte with a given value, taken from a secret key.
    The advantage with the XOR function is that using the same encryption key
    on the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
    then 107 XOR 42 = 65.

    For unbreakable encryption, the key is the same length as the plain text
    message, and the key is made up of random bytes. The user would keep the
    encrypted message and the encryption key in different locations, and
    without both "halves", it is impossible to decrypt the message.

    Unfortunately, this method is impractical for most users, so the modified
    method is to use a password as a key. If the password is shorter than the
    message, which is likely, the key is repeated cyclically throughout the
    message. The balance for this method is using a sufficiently long password
    key for security, but short enough to be memorable.

    Your task has been made easy, as the encryption key consists of three lower
    case characters. Using cipher1.txt (right click and
    'Save Link/Target As...'), a file containing the encrypted ASCII codes, and
    the knowledge that the plain text must contain common English words,
    decrypt the message and find the sum of the ASCII values in the original
    text.
    """

    with open(CIPHERS, 'r') as flr:
        chars = flr.read().strip().split(',')

    keys = list(generate_keys(97, 122, 3))

    while keys:
        decrypt = []
        key = keys.pop(0)
        for i, char in enumerate(chars):
            decrypt.append(evaluate_xored(perform_xor(int(char), key[i % 3])))
            if not decrypt[-1]:
                break
        else:
            res = ''.join([chr(value) for value in decrypt])
            if ' and ' in res:
                return sum([ord(i) for i in res])

    return None

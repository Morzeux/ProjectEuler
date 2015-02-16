'''
Created on 16.5.2014

@author: Morzeux
'''

def convert_array(arr):
    """ Converts array. """
    return ''.join([str(i) for i in arr])

def find_comb(arr):
    """ Finds combination. """
    combinations = set([])

    def comb(arr, idx):
        """ Creates new combination recursively. """
        if idx < len(arr):
            for i in range(idx, len(arr)):
                pom = arr[idx]
                arr[idx] = arr[i]
                arr[i] = pom
                combinations.add(convert_array(arr))
                comb(arr, idx + 1)
                arr[i] = arr[idx]
                arr[idx] = pom
        else:
            return 0

    comb(arr, 0)
    return sorted(list(combinations))

def problem(num=1000000, digits=10):
    """
    A permutation is an ordered arrangement of objects. For example, 3124 is
    one possible permutation of the digits 1, 2, 3 and 4. If all of the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

        012   021   102   120   201   210

    What is the millionth lexicographic permutation of the
    digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """

    digits = [i for i in range(digits)]
    return find_comb(digits)[num - 1]

'''
Created on 15.5.2014

@author: Morzeux
'''

from heapq import heappush, heappop

_DIGITS = """
75 95 64 17 47 82 18 35 87 10 20 04 82
47 65 19 01 23 75 03 34 88 02 77 73 07
63 67 99 65 04 28 06 16 70 92 41 41 26
56 83 40 80 70 33 41 48 72 33 47 32 37
16 94 29 53 71 44 65 25 43 91 52 97 51
14 70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40
31 04 62 98 27 23 09 70 98 73 93 38 53
60 04 23
"""

class Node(object):
    """ Node of Pyramid. """
    left_child = None
    right_child = None
    distance = 10000000000000000000000000000
    parent = None

    def __init__(self, count, value):
        self.count = count
        self.original_value = value

    def __lt__(self, other):
        return self.distance <= other.distance

    def set_left_child(self, child):
        """ Setter for left child. """
        self.left_child = child

    def set_right_child(self, child):
        """ Setter for right child. """
        self.right_child = child

def get_tree(digits):
    """ Creates and returns tree from array. """
    nodes = {}
    for i, val in enumerate(digits):
        nodes[i] = Node(i, val)

    i = 0
    j = 1
    for k, node in nodes.items():
        left_node = nodes.get(k + j)
        right_node = nodes.get(k + j + 1)
        node.set_left_child(left_node)
        node.set_right_child(right_node)
        i += 1
        if i % j == 0:
            j += 1
            i = 0

    max_value = max([i.original_value for i in [j for j in nodes.values()]])
    for node in nodes.values():
        node.value = max_value - node.original_value

    nodes[0].distance = nodes[0].value
    return nodes[0]

def is_shorter(parent, child):
    """ Checks if is shorter. """
    return True if parent.distance + child.value < child.distance else False

def try_append_to_queue(queue, parent, child):
    """ Evaluates path and append it to queue if shorter. """
    if is_shorter(parent, child):
        child.distance = parent.distance + child.value
        child.parent = parent
        heappush(queue, child)
        return True
    else:
        return False

def problem(digits=None):
    """
    By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.

        3
       7 4
      2 4 6
     8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

                                75
                              95 64
                            17 47 82
                          18 35 87 10
                        20 04 82 47 65
                      19 01 23 75 03 34
                    88 02 77 73 07 63 67
                  99 65 04 28 06 16 70 92
                41 41 26 56 83 40 80 70 33
              41 48 72 33 47 32 37 16 94 29
            53 71 44 65 25 43 91 52 97 51 14
          70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
      63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem
    by trying every route. However, Problem 67, is the same challenge with a
    triangle containing one-hundred rows; it cannot be solved by brute force,
    and requires a clever method! ;o)
    """
    #digits = [3, 7, 4, 2, 4, 6, 8, 5, 9, 3]
    if not digits:
        digits = [int(i.strip()) for i in
                  _DIGITS.strip().replace('\n', ' ').split(' ')]

    tree = get_tree(digits)

    queue = []

    heappush(queue, tree)
    while True:
        node = heappop(queue)
        if node.left_child and node.right_child:
            try_append_to_queue(queue, node, node.left_child)
            try_append_to_queue(queue, node, node.right_child)
        else:
            break

    path = []
    while node:
        path.append(node.original_value)
        node = node.parent

    return sum(path)

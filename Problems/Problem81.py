'''
Created on 17.5.2014

@author: Morzeux
'''

import os
from heapq import heappush, heappop

_MATRIX = os.path.join('Problems', 'matrix.txt')

class Matrix(object):
    """ Class for board matrix. """

    ALLOWED_MOVES = ['right', 'down']

    def __init__(self, width, height, nodes):
        self.width = width
        self.height = height
        self.nodes = nodes

    def _col(self, pos):
        """ Returns actual column. """
        return pos % self.width

    def _row(self, pos):
        """ Returns actual row. """
        return int(pos / self.width)

    def left(self, node):
        """ Tries to move left. """
        if self._col(node.count) > 0:
            return self.nodes[node.count - 1]
        else:
            return None

    def right(self, node):
        """ Tries to move right. """
        if self._col(node.count) < self.width - 1:
            return self.nodes[node.count + 1]
        else:
            return None

    def ups(self, node):
        """ Tries to move up. """
        if self._row(node.count) > 0:
            return self.nodes[node.count - self.width]
        else:
            return None

    def down(self, node):
        """ Tries to move down. """
        if self._row(node.count) < self.height - 1:
            return self.nodes[node.count + self.width]
        else:
            return None

    def get_start(self, start):
        """ Returns start node. """
        start = self.nodes[start]
        start.distance = start.value
        return start

    def get_last(self, finish):
        """ Returns end node. """
        return self.nodes[finish]

class Node(object):
    """ Node class. """

    distance = 10000000000000000000000000000
    parent = None

    def __init__(self, count, value):
        self.count = count
        self.value = value
        self.visited = False

    def __lt__(self, other):
        return self.distance <= other.distance

    def describe(self):
        """ Self describe. """
        return "Count: %s, Value: %s, Distance; %s" % \
            (self.count, self.value, self.distance)

    def copy(self):
        """ Copies initialized self. """
        return Node(self.count, self.value)

def load_values(demo):
    """ Loads initial board values. """
    if demo:
        return Matrix(5, 5, [Node(i, v) for i, v in enumerate([
            131, 673, 234, 103, 18,
            201, 96, 342, 965, 150,
            630, 803, 746, 422, 111,
            537, 699, 497, 121, 956,
            805, 732, 524, 37, 331])])
    else:
        with open(_MATRIX, 'r') as flr:
            digits = flr.read()
        digits = [int(i.strip()) for i in digits.strip().
                  replace('\n', ' ').replace(',', ' ').split(' ')]

        return Matrix(80, 80, [Node(i, v) for i, v in enumerate(digits)])

def solve(allowed_moves, demo=False, start_pos=0, finish_pos=-1):
    """ Solves problem to find shortest path. """
    matrix = load_values(demo)
    start = matrix.get_start(start_pos)

    def is_shorter(node, n_node):
        """ Checks if path is shorter. """
        return True if node.distance + n_node.value < n_node.distance else False

    def append_neighbours(queue, node):
        """ Adds neighbours to queue. """
        neighbours = [getattr(matrix, move)(node) for move in allowed_moves]
        neighbours = [i for i in neighbours if i]
        for n_node in neighbours:
            if is_shorter(node, n_node):
                n_node.distance = node.distance + n_node.value
                heappush(queue, n_node)
        return True

    queue = []
    heappush(queue, start)
    while True:
        node = heappop(queue)
        node.visited = True
        if (finish_pos is not True and node != matrix.get_last(finish_pos)) \
        or (finish_pos is True and \
            node.count % matrix.height != matrix.width - 1):
            append_neighbours(queue, node)
        else:
            break

    return node.distance

def problem(demo=False):
    """
    In the 5 by 5 matrix below, the minimal path sum from the top left to the
    bottom right, by only moving to the right and down, is indicated in bold
    red and is equal to 2427.

        131    673    234    103    18
        201    96    342    965    150
        630    803    746    422    111
        537    699    497    121    956
        805    732    524    37    331

    Find the minimal path sum, in matrix.txt (right click and
    'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix,
    from the top left to the bottom right by only moving right and down.
    """
    return solve(['right', 'down'], demo)

import collections

from enum import Enum

class Point(collections.namedtuple('Point', ('x', 'y'))):
    pass

class Dir(Enum):
    N = Point(0, -1)
    E = Point(1, 0)
    S = Point(0, 1)
    W = Point(-1, 0)

import math
from enum import Enum
from typing import Union


class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    UP_RIGHT = (1, -1)
    UP_LEFT = (-1, -1)
    DOWN_RIGHT = (1, 1)
    DOWN_LEFT = (-1, 1)

    @staticmethod
    def get_directions(eight=False):
        simple = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        extended = [Direction.UP, Direction.UP_RIGHT, Direction.RIGHT,
                    Direction.DOWN_RIGHT, Direction.DOWN, Direction.DOWN_LEFT,
                    Direction.LEFT, Direction.UP_LEFT]
        return extended if eight else simple

    def forward(self):
        return self

    def left(self):
        x, y = self.value
        x, y = y, -x
        return Direction((x, y))

    def right(self):
        x, y = self.value
        x, y = -y, x
        return Direction((x, y))


class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Coord):
            if self.x != other.x or self.y != other.y:
                return False
        else:
            return False
        return True

    def __hash__(self):
        prime = 31
        result = 1
        result = prime * result + self.x
        result = prime * result + self.y
        return result

    def __str__(self):
        return f'({self.x} {self.y})'

    def __repr__(self):
        return self.__str__()

    def manhattan_to(self, other: Union[tuple, 'Coord']) -> int:
        if isinstance(other, Coord):
            x, y = other.x, other.y
        elif isinstance(other, tuple) and len(other) == 2:
            x, y = other
        else:
            raise ValueError
        return abs(self.x - x) + abs(self.y - y)

    def chebyshev_to(self, other: Union[tuple, 'Coord']):
        if isinstance(other, Coord):
            x, y = other.x, other.y
        elif isinstance(other, tuple) and len(other) == 2:
            x, y = other
        else:
            raise ValueError
        return max(abs(self.x - x), abs(self.y - y))

    def get_unit_vector(self) -> 'Coord':
        x = 0 if self.x == 0 else self.x // abs(self.x)
        y = 0 if self.y == 0 else self.y // abs(self.y)
        return Coord(x, y)

    def get(self):
        return self.x, self.y

    def turn_left(self):
        return Coord(self.y, -self.x)

    def turn_right(self):
        return Coord(-self.y, self.x)

    def __add__(self, other):
        if isinstance(other, Coord):
            x, y = other.x, other.y
        elif isinstance(other, tuple) and len(other) == 2:
            x, y = other
        elif isinstance(other, int):
            x, y = other, other
        else:
            raise ValueError
        return Coord(self.x + x, self.y + y)

    def __radd__(self, other):
        if isinstance(other, (int, tuple, Coord)):
            self.__add__(other)
        else:
            raise ValueError

    def __sub__(self, other):
        if isinstance(other, Coord):
            x, y = other.x, other.y
        elif isinstance(other, tuple) and len(other) == 2:
            x, y = other
        elif isinstance(other, int):
            x, y = other, other
        else:
            raise ValueError
        return Coord(self.x - x, self.y - y)

    def __mul__(self, other):
        if isinstance(other, Coord):
            x, y = other.x, other.y
        elif isinstance(other, tuple) and len(other) == 2:
            x, y = other
        elif isinstance(other, int):
            x, y = other, other
        else:
            raise ValueError
        return Coord(self.x * x, self.y * y)
    
    def __rmul__(self, other):
        if isinstance(other, (int, tuple, Coord)):
            self.__mul__(other)
        else:
            raise ValueError

    @staticmethod
    def adjacency(eight=False):
        adj = [Coord(0, -1), Coord(1, 0), Coord(0, 1), Coord(-1, 0)]
        if eight:
            adj += [Coord(1, 1), Coord(1, -1), Coord(-1, -1), Coord(-1, 1)]
        return adj

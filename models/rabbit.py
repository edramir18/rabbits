import random
from enum import Enum

import numpy

from game.coord import Coord, Direction


class Rabbit:
    class Action(Enum):
        NOTHING = 0
        FORWARD = 'forward'
        LEFT = 'left'
        RIGHT = 'right'
        DRINK = 4
        EAT = 5

        def is_moving(self):
            return self in (self.LEFT, self.RIGHT, self.FORWARD)

        def __str__(self):
            return str(self.value)

    def __init__(self, rab_id: int, pos: Coord, seed: int):
        self.rabbit_id = rab_id
        self.pos = pos
        self.command = Rabbit.Action.NOTHING
        self.seed = seed
        self.random = numpy.random.default_rng(seed)
        self.direction = self.random.choice(Direction.get_directions())

    def run(self):
        self.command = self.random.choice([e for e in Rabbit.Action])

    def execute(self):
        print(self.command)

    def move(self):
        self.direction = getattr(self.direction, str(self.command))()
        self.pos += self.direction.value

    def check_move(self):
        delta = getattr(self.direction, str(self.command))().value
        return self.pos + delta

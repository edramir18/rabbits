from multiprocessing import Pool
from typing import Dict, List, Set

import numpy
from opensimplex import OpenSimplex

from game.cell import Cell
from game.coord import Coord
from game.grid import Grid
from models.rabbit import Rabbit


class Game:
    def __init__(self, width: int, height: int, entropy: float, seed: int,
                 population: int):
        self.width = width
        self.height = height
        self.grid = Grid(width, height)
        self.entropy = entropy
        self.is_running = True
        self.seed = seed
        self.population = population
        self.rabbits = dict()  # type: Dict[int, Rabbit]
        self.random = numpy.random.default_rng(seed)
        self.generate_grid()
        self.create_rabbits()

    def generate_grid(self):
        ground = OpenSimplex(self.seed)
        food = OpenSimplex(self.seed * 3)
        ratio = self.height / self.width
        max_x = self.width / 8
        max_y = self.height / (8 * ratio)
        water = self.entropy - 0.05
        grass = self.entropy + 0.15
        for pos, cell in self.grid.cells.items():
            rng = (ground.noise2d(pos.x / max_x, pos.y / max_y) + 1)
            rng2 = (food.noise2d(pos.x / max_x, pos.y / max_y) + 1)
            if rng < water:
                cell.celltype = Cell.CellType.WATER
            elif rng < grass:
                cell.celltype = Cell.CellType.FLOOR
            else:
                cell.celltype = Cell.CellType.FLOOR
                cell.is_grass = True
                # if rng > grass + 0.15 and rng2 > 1.50:
                #     cell.is_food = True

    @staticmethod
    def run_rabbits(rabbit: Rabbit):
        rabbit.run()
        # print(rabbit.pos, rabbit.command)
        return rabbit

    def run(self):
        # with Pool(4) as p:
        #     workers = [p.apply_async(Game.run_rabbits, args=(r,))
        #                for r in self.rabbits.values()]
        #     rabs = [worker.get() for worker in workers]
        for r in self.rabbits.values():
            r.run()
        free_cells = self.grid.get_free_cells()
        move_rabs = list()  # type: List[Rabbit]
        for r in self.rabbits.values():
            if r.command.is_moving():
                free_cells.append(r.pos)
                move_rabs.append(r)
        while True:
            move_set = set()  # type: Set[Coord]
            conflict = set()  # type: Set[Coord]
            for r in move_rabs:
                if r.command.is_moving():
                    pos = r.check_move()
                    if pos in move_set:
                        move_set.remove(pos)
                        conflict.add(pos)
                        free_cells.remove(pos)
                    elif pos not in conflict and pos in free_cells:
                        move_set.add(pos)
                    else:
                        r.command = Rabbit.Action.NOTHING
            if len(conflict) == 0:
                break
        for r in self.rabbits.values():
            if r.command.is_moving():
                self.grid.get(r.pos).has_rabbit = False
                r.move()
                self.grid.get(r.pos).has_rabbit = True

    def create_rabbits(self):
        free_cells = self.grid.get_free_cells()
        list_pos = self.random.choice(free_cells, self.population,
                                      replace=False)
        seeds = self.random.integers(0, self.population, (self.population,))
        for rabbit_id, pos in enumerate(list_pos):
            rabbit = Rabbit(rabbit_id, pos, seeds[rabbit_id])
            self.rabbits[rabbit_id] = rabbit
            self.grid.get(pos).has_rabbit = True

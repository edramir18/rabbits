from opensimplex import OpenSimplex

from game.cell import Cell
from game.grid import Grid


class Game:
    def __init__(self, width: int, height: int, entropy: float, seed: int):
        self.width = width
        self.height = height
        self.grid = Grid(width, height)
        self.entropy = entropy
        self.is_running = True
        self.seed = seed
        self.generate_grid()

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

    def run(self):
        pass

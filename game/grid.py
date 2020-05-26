from typing import Dict, List

from game.cell import Cell
from game.coord import Coord


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = dict()  # type: Dict[Coord, Cell]
        for y in range(height):
            for x in range(width):
                coord = Coord(x, y)
                cell = Cell()
                cell.celltype = Cell.CellType.FLOOR
                self.cells[coord] = cell

    def get(self, pos: Coord):
        if pos in self.cells:
            return self.cells[pos]
        return None

    def get_free_cells(self):
        return [coord for coord, cell in self.cells.items() if cell.is_empty()]

    def get_neighbourds(self, coord):
        return [coord + adj for adj in Coord.adjacency()
                if coord + adj in self.cells]

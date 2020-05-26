from enum import Enum


class Cell:
    class CellType(Enum):
        WATER = '#'
        FLOOR = ' '

        def __str__(self):
            return str(self.value)

        def __repr__(self):
            return self.__str__()

    def __init__(self):
        self.celltype = Cell.CellType.WATER
        self.is_food = False
        self.is_grass = False

    def __str__(self):
        return str(self.celltype)

    def __repr__(self):
        return self.__str__()

    def is_water(self):
        return self.celltype == Cell.CellType.WATER

    def is_floor(self):
        return self.celltype == Cell.CellType.FLOOR

    def is_empty(self):
        if self.celltype == Cell.CellType.WATER:
            return False
        return True

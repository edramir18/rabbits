import pygame as pg

from game.colors import GameColor
from game.game import Game


class GameZone:
    def __init__(self, game: Game, width: int, height: int, tile: int):
        self.width = width
        self.height = height
        self.tile = tile
        self.game = game
        self.canvas = pg.Surface((width, height))
        self.background = GameColor.BLACK.value
        self.water_color = GameColor.BLUE.value
        self.floor_color = GameColor.YELLOW.value
        self.grass_color = GameColor.GREEN.value
        self.food_color = GameColor.RED.value

    def draw(self):
        self.canvas.fill(self.grass_color)
        for coord, cell in self.game.grid.cells.items():
            if cell.is_water():
                color = self.water_color
            elif cell.is_food:
                color = self.food_color
            elif not cell.is_grass:
                color = self.floor_color
            else:
                color = None
            if color is not None:
                x, y = (coord * self.tile).get()
                pg.draw.rect(self.canvas, color,
                                (x, y, self.tile, self.tile), 0)


class GameView:
    def __init__(self, game: Game, rows: int, cols: int, tile_size: int):
        print(rows, cols)
        self.game = game
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.width = 130 + cols * tile_size
        self.height = 20 + rows * tile_size
        print(self.width, self.height)
        pg.display.set_caption("Rabbits and Fox")
        self.window = pg.display.set_mode((self.width, self.height))
        self.font = pg.font.SysFont(None, 24)
        self.font_color = GameColor.WHITE.value
        self.background = GameColor.BLUE.value
        self.zone = GameZone(game, cols * tile_size,
                             rows * tile_size, tile_size)
        self.zone.draw()
        self.update()

    def get_text(self, text):
        size = self.font.size(text)
        img = self.font.render(text, True, self.font_color, self.background)
        return size, img

    def update(self):
        self.window.blit(self.zone.canvas, (10, 10))
        pg.display.flip()

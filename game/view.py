import pygame as pg

from game.colors import GameColor
from game.game import Game


class GameView:
    def __init__(self, game: Game, rows: int, cols: int, tile_size: int):
        self.game = game
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.width = 130 + cols * tile_size
        self.height = 20 + rows * tile_size
        pg.display.set_caption("Rabbits and Fox")
        self.window = pg.display.set_mode((self.width, self.height))
        self.font = pg.font.SysFont(None, 24)
        self.font_color = GameColor.WHITE.value
        self.background = GameColor.BLUE.value
        self.window.fill(self.background)
        _, text = self.get_text('Rabbit')
        self.window.blit(text, (20 + cols * tile_size, 10))
        self.update()

    def get_text(self, text):
        size = self.font.size(text)
        img = self.font.render(text, True, self.font_color, self.background)
        return size, img

    def update(self):
        pg.display.flip()

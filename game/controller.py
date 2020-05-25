import pygame as pg

from game.game import Game


class GameController:
    def __init__(self, game: Game):
        self.game = game
        self.pause = False

    def handle_user_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN
                                         and event.key == pg.K_ESCAPE):
                self.game.is_running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.pause = not self.pause

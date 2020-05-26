#! /usr/bin/env python
import argparse

import pygame as pg

from game.config import Config
from game.controller import GameController
from game.game import Game
from game.view import GameView


def play(cfg: Config):
    pg.init()
    game = Game(**cfg.get_game_config())
    controller = GameController(game)
    view = GameView(game, **cfg.get_view_config())
    clock = pg.time.Clock()
    while game.is_running:
        clock.tick(cfg.fps)
        controller.handle_user_input()
        if not controller.pause and game.is_running:
            game.run()
            view.update()
    pg.quit()


def run(cfg: Config):
    game = Game(**cfg.get_game_config())
    game.run()


def parser_arguments():
    parser = argparse.ArgumentParser(description='Run a simulation of rabbit'
                                                 'and fox game using GA')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-p', '--play', action="store_true",
                       help='Run the simulation showing the'
                            ' graphics interface')
    group.add_argument('-r', '--replay', action="store_true",
                       help='Replay the last simulation without do any'
                            ' calculations')
    parser.add_argument('-e', '--entropy', type=float, default=0.2,
                        help='Set the entropy for the terrain generation')
    return parser.parse_args()


if __name__ == '__main__':
    parameters = parser_arguments()
    if parameters.play:
        config = Config()
        config.update(**vars(parameters))
        config.tile_size = 16
        config.width = 100
        config.height = 50
        config.save()
        play(config)
    elif parameters.replay:
        pass
    else:
        config = Config()
        config.update(**vars(parameters))
        config.save()
        if parameters.entropy:
            config.entropy = parameters.entropy
        run(config)

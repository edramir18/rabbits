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
    return parser.parse_args()


if __name__ == '__main__':
    args = parser_arguments()
    if args.play:
        config = Config()
        config.save()
        play(config)
    elif args.replay:
        pass
    else:
        pass

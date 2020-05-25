import json
import os


class Config:
    def __init__(self):
        self.fps = 24
        self.width = 20
        self.height = 20
        self.tile_size = 20

    def update(self, **kwargs):
        self.__dict__.update(kwargs)

    def save(self, filename='config/config.json'):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as jsonfile:
            json.dump(self.__dict__, jsonfile)

    def get_game_config(self):
        return {
            'width': self.width,
            'height': self.height,
        }

    def get_view_config(self):
        return {
            'rows': self.width,
            'cols': self.height,
            'tile_size': self.tile_size,
        }

    @staticmethod
    def load(filename='config/config.json'):
        with open(filename) as jsonfile:
            data = json.load(jsonfile)
            config = Config()
            config.update(**data)
        return config

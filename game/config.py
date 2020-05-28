import json
import os


class Config:
    def __init__(self):
        self.fps = 24
        self.width = 60
        self.height = 40
        self.tile_size = 16
        self.entropy = 0.35
        self.seed = 1981
        self.population = 200

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
            'entropy': self.entropy,
            'population': self.population,
            'seed': self.seed,
        }

    def get_view_config(self):
        return {
            'rows': self.height,
            'cols': self.width,
            'tile_size': self.tile_size,
        }

    @staticmethod
    def load(filename='config/config.json'):
        with open(filename) as jsonfile:
            data = json.load(jsonfile)
            config = Config()
            config.update(**data)
        return config

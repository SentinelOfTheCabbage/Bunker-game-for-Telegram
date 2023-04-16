from . import CatastropheGenerator
from . import CharacterGenerator
from . import BunkerGenerator


class Engine(CatastropheGenerator, CharacterGenerator, BunkerGenerator):

    def __init__(self):
        pass

    def get_game(self):
        pass

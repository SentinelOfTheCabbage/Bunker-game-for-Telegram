from . import MapGenerator
from . import CharacterGenerator
from . import BunkerGenerator


class Engine(MapGenerator, CharacterGenerator, BunkerGenerator):

    def __init__(self):
        pass
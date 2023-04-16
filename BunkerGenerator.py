from typing import List, Dict, Union, Tuple, Float
from . import BunkerProperties


class BunkerGenerator:

    def __init__(self):
        pass

    def _make_bunker(self):
        pass

    def get_bunker(self):
        if not self.bunker:
            self._make_bunker()
        return self.bunker
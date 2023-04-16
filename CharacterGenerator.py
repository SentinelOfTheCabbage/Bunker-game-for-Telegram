from typing import List, Dict, Union, Tuple, Float


class CharacterGenerator:

    def __init__(self, characters_count: int):
        pass

    def _make_characters(self) -> None:
        self.characters = None

    def get_characters(self):
        if not self.characters:
            self._make_characters()
        return self.characters

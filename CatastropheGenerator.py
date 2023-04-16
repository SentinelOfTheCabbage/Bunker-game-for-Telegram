from typing import List, Dict, Union, Tuple, Float


class CatastropheGenerator:

    def __init__(self, players_count: int):
        pass

    def _make_catastrophe(self) -> None:
        self.catastrophe = None

    def get_catastrophe(self) -> Tuple[Union[str, Dict[str, Float]]]:
        if not self.catastrophe:
            self._make_catastrophe()
        return self.catastrophe

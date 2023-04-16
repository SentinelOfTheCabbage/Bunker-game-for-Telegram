from time import time
from random import randrange
from Game import Engine


class Lobby:

    def __init__(self, creator):
        self.players = []
        self.creator = creator
        self.is_started = False
        self.hash = None

    def add_player(self, user):
        if not self.is_started:
            self.players.append(user.id)
            return True
        else:
            return False

    def get_hash(self):
        def get_int_hash(num):
            p = 67280421310721
            t = time()
            a = randrange(1, p)
            b = randrange(p)
            hash = hex((num * a + b) % p)[2:]
            return hash

        if getattr(self, 'hash', None):
            return self.hash
        else:
            self.hash = get_int_hash(self.creator)
            return self.hash

    def _start_game(self):
        self.is_started = True

    def create_game(self):
        self._start_game()

        engine = Engine(players_count=len(self.players()))
        self.catastrophe = engine.get_catastrophe()
        roles = engine.get_roles()
        for unit in roles:
            setattr(self.players, 'role', unit)

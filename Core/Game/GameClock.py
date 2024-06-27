from pygame.time import Clock

from Core.Game.GameRenderer import *


class GameClock:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameClock, cls).__new__(cls, *args, **kwargs)
            cls._instance._delta_time = float(0)
            cls._instance._Clock = pygame.time.Clock()
        return cls._instance

    def tick(self):
        self._delta_time = self._Clock.tick() / 1000

    @property
    def delta_time(self) -> float:
        return self._delta_time


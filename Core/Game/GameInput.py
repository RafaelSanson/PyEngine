from pygame.event import Event
from pygame.key import ScancodeWrapper

from Core.Game.GameRenderer import *


class GameInput:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameInput, cls).__new__(cls, *args, **kwargs)
            cls._instance._pressed_keys = ScancodeWrapper()
            cls._instance._events = list[Event]()
        return cls._instance

    def tick(self):
        self._events = pygame.event.get()
        self._pressed_keys = pygame.key.get_pressed()

    @property
    def events(self) -> list[Event]:
        return self._events

    @property
    def pressed_keys(self) -> ScancodeWrapper:
        return self._pressed_keys





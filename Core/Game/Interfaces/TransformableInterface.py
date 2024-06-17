from abc import ABC, abstractmethod

import pygame


class TransformableInterface(ABC):
    @property
    @abstractmethod
    def position(self) -> pygame.math.Vector2:
        pass


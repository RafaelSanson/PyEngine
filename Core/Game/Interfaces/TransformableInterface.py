from abc import ABC, abstractmethod

import pygame
from pygame import Vector2


class TransformableInterface(ABC):
    @property
    @abstractmethod
    def position(self) -> pygame.math.Vector2:
        pass

    @abstractmethod
    def translate(self, amount: Vector2):
        pass


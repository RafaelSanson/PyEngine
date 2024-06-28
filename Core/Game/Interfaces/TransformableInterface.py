from abc import ABC, abstractmethod

import pygame
from pygame import Vector2


class TransformableInterface(ABC):
    @property
    @abstractmethod
    def position(self) -> [float, float]:
        pass

    @abstractmethod
    def translate(self, x: float, y: float):
        pass


import pygame
from Core.Component import *

Vector2 = pygame.math.Vector2


class TransformComponent(Component):
    def __init__(self, owner: Actor):
        super().__init__(owner)
        self._position = Vector2((0, 0))

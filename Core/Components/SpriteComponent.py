import pygame
from pygame import Rect, Vector2, Surface

from Core.Game.GameRenderer import GameRenderer
from Core.Game.Interfaces.RendererInterface import RendererInterface
from Core.SceneComponent import *


class SpriteComponent(SceneComponent, RendererInterface):
    def __init__(self, owner, width: int, height: int):
        super().__init__(owner)
        self._surface = pygame.Surface((width, height))
        self._surface.fill((0, 255, 0))
        renderer = GameRenderer()
        renderer.register_renderer(self)

    @property
    def position(self) -> Vector2:
        return super().position
        pass

    @property
    def surface(self) -> Surface:
        return self._surface

    @property
    def rectangle(self) -> Rect:
        surface_rect = self.surface.get_rect()
        return self._compute_rect(surface_rect)

    def _compute_rect(self, surface_rect):
        return Rect(self.position.x - surface_rect.width / 2, self.position.y - surface_rect.height / 2,
                    surface_rect.width, surface_rect.height)

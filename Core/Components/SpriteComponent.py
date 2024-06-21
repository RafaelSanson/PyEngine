import pygame
from pygame import Rect, Surface, Color

from Core.Game.GameRenderer import GameRenderer
from Core.Game.Interfaces.RendererInterface import RendererInterface
from Core.SceneComponent import *


class SpriteComponent(SceneComponent, RendererInterface):
    def __init__(self, owner, width: int, height: int, color: Color):
        super().__init__(owner)
        self._surface = pygame.Surface((width, height))
        self._surface.fill(color)
        renderer = GameRenderer()
        renderer.register_renderer(self)

    @property
    def surface(self) -> Surface:
        return self._surface

    @property
    def rectangle(self) -> Rect:
        surface_rect = self.surface.get_rect()
        return self._compute_rect(surface_rect)

    def _compute_rect(self, surface_rect):
        return Rect(self.owner.position.x, self.owner.position.y,
                    surface_rect.width, surface_rect.height)

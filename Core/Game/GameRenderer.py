from typing import List

import pygame

from Core.Game.Interfaces.RendererInterface import RendererInterface

WIDTH = 1000
HEIGHT = 1000


class GameRenderer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameRenderer, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super().__init__()
        self._renderers: List[RendererInterface] = []
        self._viewport = pygame.display.set_mode((WIDTH, HEIGHT))

    def register_renderer(self, renderer: RendererInterface):
        self._renderers.append(renderer)

    def unregister_renderer(self, renderer: RendererInterface):
        self._renderers.remove(renderer)

    def draw(self):
        for renderer in self._renderers:
            surface = renderer.surface
            rectangle = renderer.rectangle
            self._viewport.blit(surface, rectangle)

        pygame.display.update()

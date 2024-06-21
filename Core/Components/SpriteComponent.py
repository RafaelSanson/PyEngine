import string

import pygame
from pygame import Rect, Surface

from Core.Assets.TextureAsset import TextureAsset
from Core.Game.GameAssetManager import GameAssetManager
from Core.Game.GameRenderer import GameRenderer
from Core.Game.Interfaces.RendererInterface import RendererInterface
from Core.SceneComponent import *


class SpriteComponent(SceneComponent, RendererInterface):
    def __init__(self, owner, width: int, height: int, texture_asset: string = "None"):
        super().__init__(owner)
        self._width = width
        self._height = height
        self._texture_asset = texture_asset
        renderer = GameRenderer()
        renderer.register_renderer(self)

    @property
    def texture(self):
        asset_manager = GameAssetManager()
        if self._texture_asset != "None":
            asset = asset_manager.get_asset(TextureAsset, self._texture_asset)
            texture = asset.load
            if isinstance(texture, Surface):
                scaled_texture = pygame.transform.scale(texture, (self._width, self._height))
                return scaled_texture

        return Surface((self._width, self._height))

    @property
    def rectangle(self) -> Rect:
        return Rect(self.owner.position.x, self.owner.position.y,
                    self._width, self._height)

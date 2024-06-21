import string

import pygame

from Core.Game.GameAssetManager import GameAssetManager
from Core.Game.Interfaces.AssetInterface import AssetInterface


class TextureAsset(AssetInterface):
    @property
    def load(self):
        directory_path = GameAssetManager().get_content_directory()
        return pygame.image.load(directory_path + self._filename)

    def __init__(self, name: string, filename: string):
        super().__init__()
        self._name = name
        self._filename = filename
        asset_manager = GameAssetManager()
        asset_manager.register_asset(TextureAsset, name, self)

import string

import pygame
from pygame import Rect, Color

from Core.Assets.TextureAsset import TextureAsset
from Core.Game.GameAssetManager import GameAssetManager
from Core.Game.GameClock import GameClock


class SpritesheetAsset(TextureAsset):
    @property
    def load(self):
        directory_path = GameAssetManager().get_content_directory()
        spritesheet_surface = pygame.image.load(directory_path + self._filename)

        self._time = (GameClock().delta_time + self._time) % self._animation_length
        index = self._time / self._animation_length * self._frames
        target_column = int(index % self._columns)
        target_row = int(index / self._columns)

        column_width = spritesheet_surface.get_rect().width / self._columns
        row_height = spritesheet_surface.get_rect().height / self._rows

        offset_x = target_column * column_width
        offset_y = target_row * row_height

        rect = Rect(offset_x, offset_y, column_width, row_height)
        frame_surface = pygame.Surface(rect.size)
        frame_surface.blit(spritesheet_surface, (0, 0), rect)
        frame_surface.set_colorkey(self._color_key)

        return frame_surface

    def __init__(self, rows: int, columns: int, frames: int, name: string, filename: string,
                 animation_length: float,
                 color_key: Color = (0, 0, 0)):
        super().__init__(name, filename)
        self._color_key = color_key
        self._name = name
        self._filename = filename
        self._animation_length = animation_length
        asset_manager = GameAssetManager()
        asset_manager.register_asset(SpritesheetAsset, name, self)

        self._rows: int = rows
        self._columns: int = columns
        self._frames: int = frames
        self._time: float = 0

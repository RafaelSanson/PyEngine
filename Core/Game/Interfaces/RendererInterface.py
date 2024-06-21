from abc import abstractmethod

from pygame import Rect

from Core.Assets.TextureAsset import TextureAsset


class RendererInterface:

    @property
    @abstractmethod
    def texture(self) -> TextureAsset:
        pass

    @property
    @abstractmethod
    def rectangle(self) -> Rect:
        pass

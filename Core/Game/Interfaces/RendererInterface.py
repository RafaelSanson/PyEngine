from abc import abstractmethod

from pygame import Surface, Rect

from Core.Game.Interfaces.TransformableInterface import TransformableInterface


class RendererInterface(TransformableInterface):

    @property
    @abstractmethod
    def surface(self) -> Surface:
        pass

    @property
    @abstractmethod
    def rectangle(self) -> Rect:
        pass

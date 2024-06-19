from abc import abstractmethod

from pygame import Surface, Rect


class RendererInterface:

    @property
    @abstractmethod
    def surface(self) -> Surface:
        pass

    @property
    @abstractmethod
    def rectangle(self) -> Rect:
        pass

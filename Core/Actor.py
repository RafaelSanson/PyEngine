from pygame import Vector2

from Core.Game.GameObject import *
from Core.Game.Interfaces.TransformableInterface import TransformableInterface
from Core.SceneComponent import SceneComponent


class Actor(GameObject, TransformableInterface):
    def __init__(self, x: int, y: int):
        super().__init__()
        self._position = Vector2(x, y)
        self._components: [SceneComponent] = []

    def add_component(self, component: SceneComponent):
        self._components.append(component)

    @property
    def position(self) -> Vector2:
        return self._position

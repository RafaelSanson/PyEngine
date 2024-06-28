from typing import List

from pygame import Vector2

from Core.Game.GameObject import *
from Core.Game.Interfaces.TransformableInterface import TransformableInterface
from Core.SceneComponent import SceneComponent


class Actor(GameObject, TransformableInterface):
    def __init__(self, x: int, y: int):
        super().__init__()
        self._position = Vector2(x, y)
        self._components: List[SceneComponent] = []

    def add_component(self, component: SceneComponent):
        self._components.append(component)

    def translate(self, x: float, y: float):
        self._position += Vector2(x, y)

    def teleport(self, x: float, y: float):
        self._position = Vector2(x, y)

    @property
    def position(self) -> Vector2:
        return self._position

    @property
    def components(self) -> List[SceneComponent]:
        return self._components

    def tick(self):
        for component in self._components:
            component.tick()

from pygame import Vector2

from Core.Game.GameObject import *
from Core.Game.Interfaces.TransformableInterface import TransformableInterface


class SceneComponent(GameObject, TransformableInterface):
    @property
    def position(self) -> Vector2:
        return self._root

    def __init__(self, root: TransformableInterface):
        super().__init__()
        self._root = root.position

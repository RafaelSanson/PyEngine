from typing import List

from Core.SceneComponent import *
from pygame import Rect, Vector2


class PhysicsComponent(SceneComponent):
    def __init__(self, owner, width: int, height: int):
        super().__init__(owner)
        self._rect = Rect(0.0, 0.0, width, height)
        self._constant_forces: List[Vector2] = []

    def add_constant_force(self, new_constant_force: Vector2):
        self._constant_forces.append(new_constant_force)

    def tick(self):
        for constant_force in self._constant_forces:
            projection = self.owner.position + constant_force
            self.owner.translate(Vector2(constant_force.x, constant_force.y))

from typing import List

from Core.Game.GameWorld import GameWorld
from Core.Game.Interfaces.RigidbodyInterface import RigidbodyInterface
from Core.SceneComponent import *
from pygame import Rect, Vector2

COLLISION_STEPS = 10


class RigidbodyComponent(SceneComponent, RigidbodyInterface):
    @property
    def is_static(self) -> bool:
        return self._static

    def _register_physics(self):
        game_world = GameWorld()
        game_world.register_physics_component(self)
        pass

    def __init__(self, owner, width: int, height: int, is_static: bool):
        super().__init__(owner)
        self._rect = Rect(0.0, 0.0, width, height)
        self._constant_forces: List[Vector2] = []
        self._velocity: Vector2 = Vector2(0, 0)
        self._static = is_static
        self._register_physics()

    def add_constant_force(self, new_constant_force: Vector2):
        self._constant_forces.append(new_constant_force)

    def tick(self):
        self._velocity = Vector2(0, 0)
        for constant_force in self._constant_forces:
            self._velocity += constant_force

    @property
    def velocity(self) -> Vector2:
        return self._velocity

    @property
    def rect(self) -> Rect:
        return self._rect

    def projected_rect(self, percentage: float) -> Rect:
        projected_position = self.owner.position + self.velocity * percentage
        projected_rect = Rect(projected_position.x, projected_position.y,
                              self.rect.width, self.rect.height)
        return projected_rect

    def project_collision(self, other: 'RigidbodyComponent') -> float:
        if other == self:
            return 1.0

        for i in range(1, COLLISION_STEPS):
            percentage: float = i / COLLISION_STEPS
            my_rect = self.projected_rect(percentage)
            other_rect = other.projected_rect(percentage)
            if my_rect.colliderect(other_rect):
                return percentage - 1 / COLLISION_STEPS if i > 1 else 0.0

        return 1.0

    def apply_velocity(self, percentage):
        self.owner.translate(self.velocity * percentage)

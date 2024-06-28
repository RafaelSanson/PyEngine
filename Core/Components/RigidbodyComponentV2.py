import math

from pygame import Vector2

from Core.Game.GameClock import GameClock
from Core.Game.GameWorld import GameWorld
from Core.Game.Interfaces.RigidbodyInterface import RigidbodyInterface
from Core.Game.Interfaces.TransformableInterface import TransformableInterface
from Core.SceneComponent import SceneComponent

ELASTICITY = 0.0
MAX_VELOCITY_LENGTH = 100.0


class RigidbodyComponentV2(SceneComponent, RigidbodyInterface):
    def add_velocity_impulse(self, impulse: Vector2):
        new_velocity = self.velocity + impulse / self.mass
        self.set_velocity(new_velocity)

    def translate(self, x: float, y: float):
        if not self.is_static:
            self.owner.translate(x, y)

    @property
    def mass(self):
        return self._mass

    @property
    def is_static(self) -> bool:
        return self._static

    @property
    def velocity(self) -> Vector2:
        return self._velocity

    @property
    def position(self) -> Vector2:
        return Vector2((self.owner.position.x + self._width / 2), (self.owner.position.y + self._height / 2))

    def __init__(self, owner: TransformableInterface, mass: float, width: float, height: float, angle, static=True):
        super().__init__(owner)
        self._mass = mass
        self._width = width
        self._height = height
        self._velocity: Vector2 = Vector2()
        self._acceleration: Vector2 = Vector2()
        self._angle = angle  # θ
        self._angular_velocity: float = 0  # ω
        self._angular_acceleration: float = 0  # α
        self._moment_of_inertia = (1 / 12) * mass * (width ** 2 + height ** 2)  # I for a rectangle
        self._static = static
        GameWorld().register_physics_component(self)

    def apply_force(self, newtonian_force_x: float, newtonian_force_y: float):
        self.apply_point_force(Vector2(newtonian_force_x, newtonian_force_y), self.position)

    def apply_point_force(self, newtonian_force: Vector2, point: Vector2):
        # Apply linear force
        self._acceleration[0] += newtonian_force[0] / self._mass
        self._acceleration[1] += newtonian_force[1] / self._mass

        # Apply torque
        # Torque = r x F (cross product)
        r = [point[0] - self.position.x, point[1] - self.position.y]
        torque = r[0] * newtonian_force[1] - r[1] * newtonian_force[0]
        self._angular_acceleration += torque / self._moment_of_inertia

    def tick_physics(self, others):
        delta_time = GameClock().delta_time / 100
        for i in range(1, 100):
            # Update linear motion
            self.set_velocity(self.velocity + self._acceleration * delta_time)
            self.translate(self.velocity.x * delta_time, self.velocity.y * delta_time)

            # Update angular motion
            self._angular_velocity += self._angular_acceleration * delta_time
            self._angle += self._angular_velocity * delta_time

            for other in others:
                self.resolve_collision(other)

        # Reset accelerations
        self._acceleration = Vector2()
        self._angular_acceleration = 0

    def get_vertices(self):
        cx, cy = self.position
        w, h = self._width / 2, self._height / 2
        angle = self._angle
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)

        return [
            (cx + w * cos_angle - h * sin_angle, cy + w * sin_angle + h * cos_angle),
            (cx - w * cos_angle - h * sin_angle, cy - w * sin_angle + h * cos_angle),
            (cx - w * cos_angle + h * sin_angle, cy - w * sin_angle - h * cos_angle),
            (cx + w * cos_angle + h * sin_angle, cy + w * sin_angle - h * cos_angle),
        ]

    @staticmethod
    def _project_polygon(axis, vertices):
        min_proj = float('inf')
        max_proj = float('-inf')
        for vertex in vertices:
            proj = vertex[0] * axis[0] + vertex[1] * axis[1]
            if proj < min_proj:
                min_proj = proj
            if proj > max_proj:
                max_proj = proj
        return min_proj, max_proj

    @staticmethod
    def _get_axes(vertices):
        axes = []
        for i in range(len(vertices)):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % len(vertices)]
            edge = (p2[0] - p1[0], p2[1] - p1[1])
            normal = (-edge[1], edge[0])
            length = math.sqrt(normal[0] ** 2 + normal[1] ** 2)
            axes.append((normal[0] / length, normal[1] / length))
        return axes

    @staticmethod
    def _overlap(min_a, max_a, min_b, max_b):
        return max_a >= min_b and max_b >= min_a

    def _sat_collision(self, other) -> [bool, Vector2]:
        vertices1 = self.get_vertices()
        vertices2 = other.get_vertices()

        axes1 = self._get_axes(vertices1)
        axes2 = self._get_axes(vertices2)

        smallest_overlap = float('inf')
        smallest_axis = None

        for axis in axes1 + axes2:
            min_a, max_a = self._project_polygon(axis, vertices1)
            min_b, max_b = self._project_polygon(axis, vertices2)
            if not self._overlap(min_a, max_a, min_b, max_b):
                return False, None
            else:
                overlap = min(max_a, max_b) - max(min_a, min_b)
                if overlap < smallest_overlap:
                    smallest_overlap = overlap
                    smallest_axis = axis

        min_translation_vector = Vector2(smallest_axis[0] * smallest_overlap, smallest_axis[1] * smallest_overlap)
        return True, min_translation_vector

    def resolve_collision(self, other: RigidbodyInterface):
        collision, min_translation_vector = self._sat_collision(other)
        if collision:
            smallest_overlap = math.sqrt(min_translation_vector.x ** 2 + min_translation_vector.y ** 2)

            # For simplicity, equally distribute the correction along the collision axis
            correction = min_translation_vector / 2

            # Move the first box by the negative correction
            self.translate(correction.x * -1, correction.y * -1)

            # Move the second box by the positive correction
            other.translate(correction.x, correction.y)

            # Adjust velocities for simple elastic collision
            normal = min_translation_vector / smallest_overlap
            relative_velocity = self.velocity - other.velocity
            velocity_along_normal = relative_velocity.x * normal.x + relative_velocity.y * normal.y

            if velocity_along_normal > 0:
                return
            # coefficient of restitution for elasticity
            impulse_scalar = -(1 + ELASTICITY) * velocity_along_normal
            impulse_scalar /= (1 / self._mass + 1 / other.mass)

            impulse = normal * impulse_scalar

            self.add_velocity_impulse(impulse * -1)
            other.add_velocity_impulse(impulse * 1)

    def set_velocity(self, new_velocity):
        length: float = new_velocity.length()
        if length <= 0:
            return
        correction_scalar = length / MAX_VELOCITY_LENGTH
        if correction_scalar > 1:
            self._velocity = new_velocity / correction_scalar
        else:
            self._velocity = new_velocity

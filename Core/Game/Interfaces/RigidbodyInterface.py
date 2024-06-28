from abc import abstractmethod


class RigidbodyInterface:

    @abstractmethod
    def translate(self, x: float, y: float):
        pass

    @abstractmethod
    def apply_force(self, newtonian_force_x: float, newtonian_force_y: float):
        pass

    @abstractmethod
    def add_velocity_impulse(self, impulse: [float, float]):
        pass

    @abstractmethod
    def apply_point_force(self, newtonian_force: float, point: [float, float]):
        pass

    @property
    @abstractmethod
    def position(self) -> [float, float]:
        pass

    @property
    @abstractmethod
    def velocity(self) -> [float, float]:
        pass

    @abstractmethod
    def resolve_collision(self, other: 'RigidbodyInterface') -> bool:
        pass

    @property
    @abstractmethod
    def is_static(self) -> bool:
        pass

    @property
    @abstractmethod
    def get_vertices(self) -> any:
        pass

    @property
    @abstractmethod
    def mass(self) -> float:
        pass

    @abstractmethod
    def tick_physics(self, objects: set['RigidbodyInterface']):
        pass

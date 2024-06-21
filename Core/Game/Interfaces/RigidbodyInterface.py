from abc import abstractmethod

from pygame import Rect


class RigidbodyInterface:
    @property
    @abstractmethod
    def rect(self) -> Rect:
        pass

    @abstractmethod
    def apply_velocity(self, percentage: float):
        pass

    @abstractmethod
    def project_collision(self, other_rigidbody) -> bool:
        pass

    @property
    @abstractmethod
    def is_static(self) -> bool:
        pass

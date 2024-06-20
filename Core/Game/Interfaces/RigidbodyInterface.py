from abc import abstractmethod

from pygame import Rect


class RigidbodyInterface:
    @property
    @abstractmethod
    def rect(self) -> Rect:
        pass

    @abstractmethod
    def apply_velocity(self):
        pass

    @abstractmethod
    def project_collision(self, other_rigidbody):
        pass

    @property
    @abstractmethod
    def is_static(self) -> bool:
        pass

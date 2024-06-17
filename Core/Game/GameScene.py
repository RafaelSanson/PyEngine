from abc import abstractmethod, ABC

from Core.Actor import Actor


class GameScene(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def load(self) -> [Actor]:
        pass


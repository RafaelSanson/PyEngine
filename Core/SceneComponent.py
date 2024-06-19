from Core.Game.GameObject import *
from Core.Game.Interfaces.TransformableInterface import TransformableInterface


class SceneComponent(GameObject):
    def __init__(self, owner: TransformableInterface):
        super().__init__()
        self.owner = owner

    def tick(self):
        pass

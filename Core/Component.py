from Actor import *
from Core.Game.GameObject import *


class Component(GameObject):
    def __init__(self, owner: Actor):
        super().__init__()
        self.owner = owner

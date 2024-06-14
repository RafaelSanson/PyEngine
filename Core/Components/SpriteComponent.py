from Core.Component import *


class SpriteComponent(Component):
    def __init__(self, owner: Actor):
        super().__init__(owner)

    def draw(self):
        transform = super().owner.transform
        
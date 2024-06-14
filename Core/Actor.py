from Component import Component
from Components.TransformComponent import TransformComponent
from Core.Game.GameObject import *
from typing import List


class Actor(GameObject):
    def __init__(self):
        super().__init__()
        self._transform = TransformComponent(self)
        self._components: List[Component] = []

    def add_component(self, component: Component):
        self._components.append(component)

    @property
    def transform(self):
        return self._transform


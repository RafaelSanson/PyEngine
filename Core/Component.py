from Actor import *
from Object import *


class Component(Object):
    def __init__(self, owner: Actor):
        super().__init__()
        self.owner = owner

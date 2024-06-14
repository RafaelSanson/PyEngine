from Core.Game.GameObject import *


class GameRenderer(GameObject):
    def __init__(self):
        super().__init__()
        self.renderers = []

    def register_renderer(self, renderer):
        self.renderers.append(renderer)

    def unregister_renderer(self, renderer):
        self.renderers.remove(renderer)

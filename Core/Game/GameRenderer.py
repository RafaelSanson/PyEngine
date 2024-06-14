from Core.Object import *


class GameRenderer(Object):
    def __init__(self):
        super().__init__()
        self.renderers = []

    def register_renderer(self, renderer):
        self.renderers.append(renderer)

    def unregister_renderer(self, renderer):
        self.renderers.remove(renderer)

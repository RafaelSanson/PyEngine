from Core.Game.GameLog import GameLog
from Core.Game.GameRenderer import *
from Core.Game.GameScene import *
from Core.Game.GameWorld import GameWorld

WIDTH = 1000
HEIGHT = 1000
FPS = 144


class GameApplication:
    def __init__(self):
        super().__init__()
        self._GameRenderer = GameRenderer()
        self._GameWorld = GameWorld(self._GameRenderer)
        self._GameLog = GameLog()
        self._Clock = pygame.time.Clock()

    def loop(self):
        while True:
            self._GameWorld.tick()
            self._GameRenderer.draw()
            self. _Clock.tick(FPS)

    def load_scene(self, scene: GameScene):
        self._GameWorld.load_scene(scene)

from Core.Game.GameAssetManager import GameAssetManager
from Core.Game.GameClock import GameClock
from Core.Game.GameLog import GameLog
from Core.Game.GameRenderer import *
from Core.Game.GameScene import *
from Core.Game.GameWorld import GameWorld


class GameApplication:
    def __init__(self):
        super().__init__()
        self._delta_time: int = 0
        self._GameRenderer = GameRenderer()
        self._GameWorld = GameWorld()
        self._GameLog = GameLog()
        self._GameAssetManager = GameAssetManager()
        self._GameClock = GameClock()

    def start(self):
        while True:
            self._GameWorld.tick()
            self._GameWorld.tick_physics()
            self._GameRenderer.draw()
            self._GameClock.tick()

    def load_scene(self, scene: GameScene):
        self._GameWorld.load_scene(scene)

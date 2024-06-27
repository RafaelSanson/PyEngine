import pygame

from Core.Game.GameAssetManager import GameAssetManager
from Core.Game.GameClock import GameClock
from Core.Game.GameInput import GameInput
from Core.Game.GameLog import GameLog
from Core.Game.GameRenderer import GameRenderer
from Core.Game.GameScene import GameScene
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
        self._GameInput = GameInput()

    def start(self):
        pygame.init()
        while True:
            self._GameInput.tick()
            self._GameWorld.tick()
            self._GameWorld.tick_physics()
            self._GameRenderer.draw()
            self._GameClock.tick()

    def load_scene(self, scene: GameScene):
        self._GameWorld.load_scene(scene)

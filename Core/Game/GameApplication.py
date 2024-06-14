from Core.Game.GameLog import GameLog
from Core.Game.GameRenderer import *
from Core.Game.GameScene import *


class GameApplication:
    def __init__(self):
        super().__init__()
        self._GameWorld = GameScene()
        self._GameRenderer = GameRenderer()
        self._GameScenes = []
        self._GameLog = GameLog()

from typing import List

from Core.Actor import Actor
from Core.Game.GameRenderer import GameRenderer
from Core.Game.GameScene import GameScene


class GameWorld:
    def __init__(self, renderer: GameRenderer):
        super().__init__()
        self._actors: List[Actor] = []
        self._current_scene = None
        self._renderer = renderer

    def load_scene(self, scene: GameScene):
        self._current_scene = scene
        new_actors = self._current_scene.load()
        self._actors.extend(new_actors)

    def tick(self):
        for actor in self._actors:
            actor.tick()

from typing import List

from Core.Actor import Actor
from Core.Components.SpriteComponent import SpriteComponent
from Core.Game.GameApplication import GameApplication
from Core.Game.GameScene import GameScene


class SandboxApplication(GameApplication):
    def __init__(self):
        super().__init__()


class SandboxScene(GameScene):
    def load(self):
        actors: List[Actor] = []
        actor = Actor(250, 250)
        actor.add_component(SpriteComponent(actor, 100, 100))
        return actors


app = SandboxApplication()
app.load_scene(SandboxScene())
app.loop()

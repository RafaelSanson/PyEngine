from typing import List

from Core.Actor import Actor
from Core.Game.GameApplication import GameApplication
from Core.Game.GameAssetManager import GameAssetManager
from Core.Game.GameScene import GameScene
from Examples.RefactoredPlatformTutorial.Game.BackgroundActor import BackgroundActor
from Examples.RefactoredPlatformTutorial.Game.LandscapeActor import LandscapeActor
from Examples.RefactoredPlatformTutorial.Game.SnowmanActor import SnowmanActor


class PlatformScene(GameScene):
    def load(self):
        actors: List[Actor] = []
        GameAssetManager().set_content_directory("Examples\\RefactoredPlatformTutorial\\Content\\")
        actors.append(BackgroundActor(0, 0))
        actors.append(SnowmanActor(250, 250))
        actors.append(LandscapeActor(0, 950))
        return actors


app = GameApplication()
app.load_scene(PlatformScene())
app.start()

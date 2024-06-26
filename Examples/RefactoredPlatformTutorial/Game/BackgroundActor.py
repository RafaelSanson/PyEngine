from Core.Actor import Actor
from Core.Assets.TextureAsset import TextureAsset
from Core.Components.SpriteComponent import SpriteComponent


class BackgroundActor(Actor):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        TextureAsset("Background", "background.png")
        self.add_component(SpriteComponent(self, 1000, 1000, "Background"))

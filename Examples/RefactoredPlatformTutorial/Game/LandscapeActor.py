from Core.Actor import Actor
from Core.Assets.TextureAsset import TextureAsset
from Core.Components.RigidbodyComponentV2 import RigidbodyComponentV2
from Core.Components.SpriteComponent import SpriteComponent


class LandscapeActor(Actor):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        TextureAsset("Platform", "platform.png")
        self.jumping = False
        self.score = 0
        self.add_component(SpriteComponent(self, 1000, 50, "Platform"))

        physics_component = RigidbodyComponentV2(self, 1000000, 1000, 50, 0)
        self.add_component(physics_component)

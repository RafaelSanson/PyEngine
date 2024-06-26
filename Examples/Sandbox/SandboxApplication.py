from typing import List

from pygame import Vector2

from Core.Actor import Actor
from Core.Assets.SpritesheetAsset import SpritesheetAsset
from Core.Assets.TextureAsset import TextureAsset
from Core.Components.RigidbodyComponent import RigidbodyComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.Game.GameApplication import GameApplication
from Core.Game.GameAssetManager import GameAssetManager
from Core.Game.GameScene import GameScene


class SandboxApplication(GameApplication):
    def __init__(self):
        super().__init__()


class SandboxScene(GameScene):
    def load(self):
        actors: List[Actor] = []

        GameAssetManager().set_content_directory("Examples\\Sandbox\\Content\\")
        SpritesheetAsset(1, 24, 2, "Player", "doux.png", 0.5)

        # TextureAsset("Player", "snowman.png")
        TextureAsset("Background", "background.png")
        TextureAsset("Platform", "platform.png")

        background_actor = Actor(0, 0)
        background_sprite_component = SpriteComponent(background_actor, 1000, 1000, "Background")
        background_actor.add_component(background_sprite_component)
        actors.append(background_actor)

        player = Actor(250, 250)
        player_sprite_component = SpriteComponent(player, 100, 100, "Player")
        player.add_component(player_sprite_component)

        physics_component = RigidbodyComponent(player, 100, 100, False)
        physics_component.add_constant_force(Vector2(0, 980))
        player.add_component(physics_component)
        actors.append(player)

        landscape = Actor(0, 950)
        landscape_sprite_component = SpriteComponent(landscape, 1000, 50, "Platform")
        landscape.add_component(landscape_sprite_component)

        landscape_physics_component = RigidbodyComponent(landscape, 1000, 50, True)
        landscape.add_component(landscape_physics_component)
        actors.append(landscape)

        return actors


app = SandboxApplication()
app.load_scene(SandboxScene())
app.start()

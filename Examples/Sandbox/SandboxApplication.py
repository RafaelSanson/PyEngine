from typing import List

from pygame import Vector2, Color

from Core.Actor import Actor
from Core.Components.RigidbodyComponent import RigidbodyInterface, RigidbodyComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.Game.GameApplication import GameApplication
from Core.Game.GameScene import GameScene


class SandboxApplication(GameApplication):
    def __init__(self):
        super().__init__()


class SandboxScene(GameScene):
    def load(self):
        actors: List[Actor] = []

        background_actor = Actor(500, 500)
        background_sprite_component = SpriteComponent(background_actor, 1000, 1000, Color(127, 127, 127))
        background_actor.add_component(background_sprite_component)
        actors.append(background_actor)

        player = Actor(250, 250)
        player_sprite_component = SpriteComponent(player, 100, 100, Color(0, 255, 0))
        player.add_component(player_sprite_component)

        physics_component = RigidbodyComponent(player, 100, 100, False)
        physics_component.add_constant_force(Vector2(0, 5))
        player.add_component(physics_component)
        actors.append(player)

        landscape = Actor(0, 1000)
        landscape_sprite_component = SpriteComponent(landscape, 10000, 50, Color(0, 255, 0))
        landscape.add_component(landscape_sprite_component)

        landscape_physics_component = RigidbodyComponent(landscape, 10000, 50, True)
        landscape.add_component(landscape_physics_component)
        actors.append(landscape)

        return actors


app = SandboxApplication()
app.load_scene(SandboxScene())
app.loop()

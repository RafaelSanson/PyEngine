from Core.Actor import Actor
from Core.Game.GameScene import GameScene
from Core.Game.Interfaces.RigidbodyInterface import RigidbodyInterface


class GameWorld:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameWorld, cls).__new__(cls, *args, **kwargs)
            cls._actors: list[Actor] = list()
            cls._physics_components_static: set[RigidbodyInterface] = set()
            cls._physics_components_dynamic: set[RigidbodyInterface] = set()
            cls._current_scene: GameScene = GameScene()
        return cls._instance

    def load_scene(self, scene: GameScene):
        self._current_scene = scene
        new_actors = self._current_scene.load()
        self._actors.extend(new_actors)

    def register_physics_component(self, rigidbody: RigidbodyInterface):
        if rigidbody.is_static:
            self._physics_components_static.add(rigidbody)
        else:
            self._physics_components_dynamic.add(rigidbody)

    def tick(self):
        for actor in self._actors:
            actor.tick()

    def tick_physics(self):
        for dynamic_object in self._physics_components_dynamic:
            other_objects = set(self._physics_components_dynamic)
            other_objects.update(self._physics_components_static)
            other_objects.remove(dynamic_object)
            dynamic_object.tick_physics(other_objects)


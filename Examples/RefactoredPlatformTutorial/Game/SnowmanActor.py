import pygame
from pygame.locals import *

from Core.Actor import Actor
from Core.Assets.TextureAsset import TextureAsset
from Core.Components.RigidbodyComponent import RigidbodyComponent
from Core.Components.SpriteComponent import SpriteComponent
from Core.Game.GameInput import GameInput


class SnowmanActor(Actor):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        TextureAsset("Player", "snowman.png")
        self.jumping = False
        self.score = 0
        self.add_component(SpriteComponent(self, 100, 100, "Player"))

        self._physics_component = RigidbodyComponent(self, 100, 100, False)
        self._physics_component.add_constant_force(0, 980)
        self.add_component(self._physics_component)

    def tick(self):
        super().tick()
        self.process_keyboard_input()

    def process_keyboard_input(self):
        pressed_keys = GameInput().pressed_keys
        if pressed_keys:
            if pressed_keys[K_LEFT]:
                self._physics_component.add_one_time_impulse(-100, 0)
            if pressed_keys[K_RIGHT]:
                self._physics_component.add_one_time_impulse(100, 0)

        for event in GameInput().events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._physics_component.add_one_time_impulse(0, -4000)

        if self.position.x > 1000:
            self.teleport(0, self.position.y)
        if self.position.x < 0:
            self.teleport(1000, self.position.y)

    # def jump(self):
    #     hits = pygame.sprite.spritecollide(self, platforms, False)
    #     if hits and not self.jumping:
    #         self.jumping = True
    #         self.vel.y = -15
    #
    # def cancel_jump(self):
    #     if self.jumping:
    #         if self.vel.y < -3:
    #             self.vel.y = -3

    # def update(self):
    #     hits = pygame.sprite.spritecollide(self, platforms, False)
    #     if self.vel.y > 0:
    #         if hits:
    #             if self.pos.y < hits[0].rect.bottom:
    #                 if hits[0].point == True:
    #                     hits[0].point = False
    #                     self.score += 1
    #                 self.pos.y = hits[0].rect.top + 1
    #                 self.vel.y = 0
    #                 self.jumping = False

from pygame import Vector2

from Core.Actor import Actor
from Core.Assets.TextureAsset import TextureAsset
from Core.Components.RigidbodyComponent import RigidbodyComponent
from Core.Components.SpriteComponent import SpriteComponent


class SnowmanActor(Actor):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        TextureAsset("Player", "snowman.png")
        self.jumping = False
        self.score = 0
        self.add_component(SpriteComponent(self, 100, 100, "Player"))

        physics_component = RigidbodyComponent(self, 100, 100, False)
        physics_component.add_constant_force(Vector2(0, 980))
        self.add_component(physics_component)

    # def move(self):
    #     self.acc = vec(0, 0.5)
    #
    #     pressed_keys = pygame.key.get_pressed()
    #
    #     if pressed_keys[K_LEFT]:
    #         self.acc.x = -ACC
    #     if pressed_keys[K_RIGHT]:
    #         self.acc.x = ACC
    #
    #     self.acc.x += self.vel.x * FRIC
    #     self.vel += self.acc
    #     self.pos += self.vel + 0.5 * self.acc
    #
    #     if self.pos.x > WIDTH:
    #         self.pos.x = 0
    #     if self.pos.x < 0:
    #         self.pos.x = WIDTH
    #
    #     self.rect.midbottom = self.pos

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
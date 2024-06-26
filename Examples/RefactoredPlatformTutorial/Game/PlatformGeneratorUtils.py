def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform, groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 40) and (
                    abs(platform.rect.bottom - entity.rect.top) < 40):
                return True
        C = False


def plat_gen():
    while len(platforms) < 6:
        width = random.randrange(50, 100)
        p = None
        C = True

        while C:
            p = platform()
            p.rect.center = (random.randrange(0, WIDTH - width),
                             random.randrange(-50, 0))
            C = check(p, platforms)

        p.generateCoin()
        platforms.add(p)
        all_sprites.add(p)
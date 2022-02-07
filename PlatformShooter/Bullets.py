import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.transform.flip(pygame.image.load('TeamGunner_By_SecretHideout_060519/EXTRAS/SpongeBullet.png'), True, False).convert_alpha()
        self.rect = self.image.get_rect(center= position)

    def update(self, projectile_speed):
        self.rect.x += projectile_speed

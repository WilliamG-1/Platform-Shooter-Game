import pygame
from Tiles import Tile

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = pygame.transform.flip(pygame.image.load('Assets/Enemy/Idle/0.png'), True, False).convert_alpha()
        self.rect = self.image.get_rect(topleft = position)





    def update(self, shift_in_x):
        self.rect.x += shift_in_x



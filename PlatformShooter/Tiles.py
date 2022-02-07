import pygame
from Level import *
from player import Player

class Tile(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('TeamGunner_By_SecretHideout_060519/EXTRAS/Platform.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (position))

    def update(self, shift_x):
        self.rect.x += shift_x





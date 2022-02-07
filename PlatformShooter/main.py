import sys
import pygame
from platform import Platform
from Tiles import Tile
from player import Player
from Level import *
from Time import Timer
# Initialize Pygame
pygame.init()



screen = pygame.display.set_mode((screen_width, screen_height))

draw = Platform(screen)


clock = pygame.time.Clock()

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 100)
simp_timer = Timer()
while True:

    screen.fill((100, 150, 180))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    simp_timer.timing()
    draw.run()
    pygame.display.update()

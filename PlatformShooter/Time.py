import pygame
import math

class Timer():
    def __init__(self):
        self.clock = 0


    def timing(self):
        self.clock = int(pygame.time.get_ticks() / 1000)
        if self.clock >= 3:
            self.clock -= 3
        print(self.clock)


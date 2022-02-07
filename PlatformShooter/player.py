import pygame
from Level import *
from file_names import find_files
from os import path
from Bullets import Bullet


class Player(pygame.sprite.Sprite):


    def __init__(self, position):
        super().__init__()


        # Player Sprites
        self.image = pygame.image.load(r'Assets/Idle/Idle1.png').convert_alpha()
        self.f0 = pygame.image.load(r'Assets/Running/0.png').convert_alpha()
        self.f1 = pygame.image.load(r'Assets/Running/1.png').convert_alpha()
        self.f2 = pygame.image.load(r'Assets/Running/2.png').convert_alpha()
        self.f3 = pygame.image.load(r'Assets/Running/3.png').convert_alpha()
        self.f4 = pygame.image.load(r'Assets/Running/4.png').convert_alpha()
        self.f5 = pygame.image.load(r'Assets/Running/5.png').convert_alpha()
        self.frame = 0  # Index number for frame

        self.animations = {'Running': [], 'Idle': []}
        self.file_path = 'Idle'

        self.allow_rotate = True  # Checks if the sprite is allowed to rotate
        self.rotated_l = False  # Chekcs if sprite is facing left (Facing right by default)
        self.grounded = False
        self.c_right = False
        self.c_left = False
        self.shoot = False

        self.direction = pygame.math.Vector2(0,0)

        self.rect = self.image.get_rect(topleft=(position))

        self.gravity = .5
        self.jump_speed = -12
        self.movespeed = 99
        self.movement = 0  # Value Identifier for animation, 0 = Idle 1 = Right, 2 = Left

        self.bullets = pygame.sprite.Group()

    def player_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1.2
            self.movement = 2

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.movement = 1
            self.direction.x = 1.2
        else:
            self.movement = 0
            self.direction.x = 0
            self.allow_rotate = True

        if keys[pygame.K_SPACE] and self.grounded:
            self.jump()

        if keys[pygame.K_p]:
            self.shoot = True
        else: self.shoot = False



        if not any(keys):
            self.movement = 0
            self.direction.x = 0
            self.allow_rotate = True



        #
        # if keys[pygame.K_UP]:
        #     self.power = True

    def retrieve_images(self):
        if self.frame == 1 or self.frame == 2:
            self.file_path = "Running"
        for animation_playing in self.animations.keys():
            self.animations[animation_playing] = find_files(self.file_path)

    def player_animation(self):
        animation = self.animations['Idle']

        if self.movement == 0:
            if not self.rotated_l:
                self.frame += .09
                if self.frame >= len(animation):
                    self.frame = 0
                self.image = pygame.image.load(path.join('Assets', self.file_path, animation[int(self.frame)]))
            else:
                self.frame += .09
                if self.frame >= len(animation):
                    self.frame = 0
                self.image = pygame.transform.flip(
                    pygame.image.load(path.join('Assets', self.file_path, animation[int(self.frame)])), True, False)

        if self.movement == 1:
            # self.rotated_l = False
            # animation = self.animations['Running']
            # self.frame += .15
            # if self.frame >= len(animation):
            #     self.frame = 0
            # self.image = pygame.image.load(path.join('Assets', self.file_path , animation[int(self.frame)]))

            if self.allow_rotate and self.rotated_l:
                self.rotated_r = True  # Player is facing right
                # flip the sprite's image horizontally
                self.f0 = pygame.transform.flip(self.f0, True, False)
                self.f1 = pygame.transform.flip(self.f1, True, False)
                self.f2 = pygame.transform.flip(self.f2, True, False)
                self.f3 = pygame.transform.flip(self.f3, True, False)
                self.f4 = pygame.transform.flip(self.f4, True, False)
                self.f5 = pygame.transform.flip(self.f5, True, False)
                self.rotated_l = False  # Player is not facing left

            self.allow_rotate = False  # While key is held, player cannot turn

            self.frame += .12
            if self.frame >= 5: self.frame = 0
            # Frame Order:   4, 5, 3, 0, 1, 2
            running_list = [self.f0, self.f1, self.f2, self.f4, self.f5, self.f3, self.f2]
            self.image = running_list[int(self.frame)]

        if self.movement == 2:

            if self.allow_rotate and not self.rotated_l:
                self.rotated_l = True  # Player is now facing left
                # Flips the sprite image horizontally
                self.f0 = pygame.transform.flip(self.f0, True, False)
                self.f1 = pygame.transform.flip(self.f1, True, False)
                self.f2 = pygame.transform.flip(self.f2, True, False)
                self.f3 = pygame.transform.flip(self.f3, True, False)
                self.f4 = pygame.transform.flip(self.f4, True, False)
                self.f5 = pygame.transform.flip(self.f5, True, False)

            self.allow_rotate = False  # While key is held, player cannot turn

            self.frame += .12  # increase to choose next index value (Controls the animation speed)

            if self.frame >= 5: self.frame = 0  # Restarts counter to avoid index out of range
            running_list = [self.f0, self.f1, self.f2, self.f4, self.f5, self.f3,
                            self.f2]  # List for frames available to iterate over

            self.image = running_list[int(self.frame)]  # Selects the image from the current index



    def cool_spin_power(self):
        if self.power:  # if item is in inventory: do this
            self.image = pygame.transform.rotate(self.image, 90)

    def apply_gravity(self):
        keys = pygame.key.get_pressed()
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    # In a relationship, it's important to establish boundaries!
    def death(self):
        if self.rect.y >= 680:
            self.rect.y = -700
            self.rect.x += 80
            self.direction.y = 1

    # def draw(self):
    #     self.screen.blit(self.image, self.rect)


    def update(self):

        if self.c_left: print('collideleft')
        self.rect.x += self.movespeed * self.direction.x
        self.player_input()
        self.retrieve_images()
        self.player_animation()
        self.death()


import pygame
from Level import *
from Tiles import Tile
from player import Player
from Enemies import  Enemy
from Bullets import Bullet
from Time import Timer

class Platform(pygame.sprite.Sprite):

    def __init__(self,surface):
        self.surface = surface
        self.draw_platforms()
        self.current_x = 0
        self.ctr = 0
        self.enemy_positions = []
        self.enemy_shoot()

    def draw_platforms(self):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.herobullets = pygame.sprite.Group()
        print('doing')
        for r_index, row in enumerate(level_setup):
            for col_index, col in enumerate(row):
                y = r_index * tile_size
                x = col_index * tile_size
                if col == 'O':
                    tile = Tile((x,y))
                    self.tiles.add(tile)
                if col == 'P':
                    p = Player((x,y))
                    self.player.add(p)
                if col == "E":
                    enemy = Enemy((x,y))
                    self.enemies.add(enemy)

    def horizontal_collision(self):
        player = self.player.sprite

        for i in self.tiles.sprites():
            if i.rect.colliderect(player.rect):
                x = player.rect.x
                y = player.rect.y
                if player.direction.x > 0: # Moving Right
                    player.rect.right = i.rect.left
                    player.c_right = True
                    self.current_x = player.rect.right


                elif player.direction.x < 0:
                    player.c_left = True

                    player.rect.left = i.rect.right
                    self.current_x = player.rect.left

            if player.c_right and (player.rect.right >= self.current_x or player.direction.x >= 0):
                player.c_right = False

            if player.c_left and (player.rect.left <= self.current_x or player.direction.x >= 0):
                player.c_left = False
    def vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for i in self.tiles.sprites():
            if i.rect.colliderect(player.rect):
                if player.direction.y >= 0:

                    player.rect.bottom = i.rect.top
                    player.direction.y = 0
                    player.grounded = True

                elif player.direction.y < 0:
                    player.direction.y = 0
                    print('bottom')
                    player.rect.top = i.rect.bottom

        if player.grounded and player.direction.y < 0 or player.direction.y > .8:

            player.grounded = False
    def player_sprite(self):

        player_sprite = self.player.sprite
        player_x = player_sprite.rect.centerx
        direction_x = player_sprite.direction.x
        if player_x <= 200 and direction_x < 0:
            player_sprite.movespeed = 0
            self.tiles.update(4)
            self.enemies.update(4)
            self.bullets.update(2.5)
        elif player_x >= 600 and direction_x > 0:
            player_sprite.movespeed = 0
            self.tiles.update(-4)
            self.enemies.update(-4)
            self.bullets.update(-2.5)

        else:
            player_sprite.movespeed = 4



    def enemy_shoot(self):
        # Create the Bullets sprite group


        self.bullets = pygame.sprite.Group()
        # Loop through all the enemies' sprites
        for sprite in self.enemies.sprites():
            self.enemy_positions.append(sprite.rect.midleft) # Append their position to a list, which can then be accessed

        for pos in self.enemy_positions:
            bullet = Bullet(pos) # Add a bullet sprite at the position of an enemies list
            self.bullets.add(bullet)
        # Add the object to the list of sprites

    def enemy_reload(self):
        for bullet in self.bullets.sprites():
             if bullet.rect.x <= -50:
                for enemy in self.enemies.sprites():
                    if bullet.rect.y in range((enemy.rect.y -20), (enemy.rect.y + 20)):
                        self.bullets.remove(bullet)
                        bullet = Bullet(enemy.rect.midleft)
                        self.bullets.add(bullet)

    def player_shoot(self):
        if self.player.sprite.shoot:
            hero_bullet = Bullet(self.player.sprite.rect.midright)
            self.herobullets.add(hero_bullet)
        self.herobullets.draw(self.surface)



    def run(self):


        self.player.update()
        self.player.draw(self.surface)
        self.bullets.draw(self.surface)
        self.tiles.draw(self.surface)
        self.enemies.draw(self.surface)
        self.player_sprite()
        self.horizontal_collision()
        self.vertical_collision()
        self.bullets.update(-2.5)
        self.enemy_reload()
        self.player_shoot()
        self.herobullets.update(9.5)



        # self.tiles.shift(1)







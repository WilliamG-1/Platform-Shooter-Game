import sys

import pygame




class Surface(pygame.sprite.Sprite):
    def __init__(self, width, height, xpos, ypos, color):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.x = xpos
        self.y = ypos
        self.rect = self.image.get_rect(center = (self.x,self.y))

    def move(self):

        self.x += 10
        print('hi')


    def draw(self):
        pass

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/Idle/Idle1.png').convert_alpha()
        self.rect = self.image.get_rect(center = (100,200))
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 9.8

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    def apply_gravity(self):

        pass


    def Update(self):
        self.movement()
        self.rect.x += self.direction.x * self.speed



class draw(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = pygame.sprite.GroupSingle()

    def draw(self):

        self.player.add(player)
        self.player.draw(screen)
        self.player.update()

    def scroll(self):
        player_sprite = self.player.sprite
        player_x = player_sprite.rect.centerx
        direction_x = player.direction.x

        if player_x == 200:
            pass

pygame.init()
screen = pygame.display.set_mode((800,600))

# Platform group
platform_group = pygame.sprite.Group()
platform = Surface(32,64,400,300, (225,10,10))
platform2 = Surface(32,64,500,300, (10,10,225))
platform_group.add(platform)
platform_group.add(platform2)

# Player Group

player = Player()
test = draw()

# player_group = pygame.sprite.Group()
# player1 = Player((600,400))
# player_group.add(player1)






clock = pygame.time.Clock()

while True:

    screen.fill((120, 255, 255))
    clock.tick(60)
    keys_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if keys_pressed[pygame.K_LEFT]:
        pass
        # if pygame.sprite.spritecollide(platform_group, rect, False):
        #     print('hi')


    platform_group.draw(screen)

    if pygame.sprite.spritecollide(player,platform_group, False):
        print('hi')
    test.draw()
    player.Update()
    pygame.display.update()

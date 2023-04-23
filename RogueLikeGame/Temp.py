import pygame
import random
from pygame.locals import (RLEACCEL,KEYDOWN,K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,QUIT)


WIDTH = 900
HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey(('white'),RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self,pressed):
        if pressed[K_UP]:
            self.rect.move_ip(0,-5)
            move_up_sound.play()
        elif pressed[K_DOWN]:
            self.rect.move_ip(0,5)
            move_down_sound.play()
        elif pressed[K_LEFT]:
            self.rect.move_ip(-5,0)
        elif pressed[K_RIGHT]:
            self.rect.move_ip(5,0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey(('white'),RLEACCEL)
        self.rect = self.surf.get_rect(center = (random.randint(WIDTH+20,WIDTH+100), random.randint(0,HEIGHT)))
        self.speed = random.randint(5,20)
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud,self).__init__()
        self.surf=pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey(("black"),RLEACCEL)
        self.rect = self.surf.get_rect(center=(random.randint(WIDTH+20,WIDTH+100),random.randint(0,HEIGHT)))
    def update(self):
        self.rect.move_ip(-5,0)
        if self.rect.right < 0:
            self.kill()
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)
move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Collision.ogg")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH,HEIGHT])

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY,250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD,1000)

player = Player()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
all_sprites.add(player)



running = True
while (running == True):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy=Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
    enemies.update()
    clouds.update()
    screen.fill(('sky blue'))
    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect)
    player.update(pygame.key.get_pressed())
    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()
        move_down_sound.stop()
        move_up_sound.stop()
        collision_sound.play()
        running = False
    pygame.display.flip()
    clock.tick(60)
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()

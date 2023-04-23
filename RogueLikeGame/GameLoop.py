import pygame, numpy
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT)
from Map.Map import *
from Player.Player import Player
from SpriteSheet.sprite_sheet import Spritesheet
from Enemy.Enemy import *

WIDTH = 1024
HEIGHT = 768
fake_width = -2
fake_height = -382
###
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu')
        self.setGeometry(700,200,250,100)
        self.setStyleSheet("background-color: gray")
        self.setWindowIcon(QIcon('unnamed.png'))
        self.UIComponents()
        self.show()

    def UIComponents(self):
        self.start = QPushButton('Start',self)
        self.start.setGeometry(QtCore.QRect(75,10,100,25))
        self.start.setStyleSheet("border-radius: 10px; border: 2px solid black; background-color: white")
        self.start.clicked.connect(self.clicked1)

        self.closing = QPushButton('Close',self)
        self.closing.setGeometry(QtCore.QRect(75,60,100,25))
        self.closing.setStyleSheet("border-radius: 10px; border: 2px solid black; background-color: white")
        self.closing.clicked.connect(self.clicked2)

    def clicked1(self):
        self.close()

    def clicked2(self):
        self.close()
        exit() ##Menu
pygame.init()
app = QApplication([])
menu = Menu()
app.exec_()
programIcon = pygame.image.load('unnamed.png')
pygame.display.set_icon(programIcon)
canvas = pygame.Surface((WIDTH,HEIGHT))
screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
running = True
player = Player(140, 650) #340,520
player.rect.x, player.rect.y = 140,650 #140,650 #200, 100

checkpoint1 = Checkpoint(490,500)
checkpoint2 = Checkpoint(65,173)

enemy1 = Moving_Enemy(300,120)

###
def Sprites_init():
    object_list=[]
    ###
    spikes1 = Enemy('Enemy\Pit_Trap_Spikes.png',307,605,0)
    spikes2 = Enemy('Enemy\Pit_Trap_Spikes.png',339,605,0)
    spikes3 = Enemy('Enemy\Pit_Trap_Spikes.png',355,605,0)
    spikes4 = Enemy('Enemy\Pit_Trap_Spikes.png',387,605,0)
    spikes5 = Enemy('Enemy\Pit_Trap_Spikes.png',407,605,0)
    spikes6 = Enemy('Enemy\Pit_Trap_Spikes.png',407,635,0)
    spikes7 = Enemy('Enemy\Pit_Trap_Spikes.png',407,665,0)
    spikes8 = Enemy('Enemy\Pit_Trap_Spikes.png',187,482,0)
    spikes9 = Enemy('Enemy\Pit_Trap_Spikes.png',127,482,0)
    spikes10 = Enemy('Enemy\Pit_Trap_Spikes.png',67,482,0)
    ###
    enemies.add(spikes1)
    enemies.add(spikes2)
    enemies.add(spikes3)
    enemies.add(spikes4)
    enemies.add(spikes5)
    enemies.add(spikes6)
    enemies.add(spikes7)
    enemies.add(spikes8)
    enemies.add(spikes9)
    enemies.add(spikes10)
    enemies.add(enemy1)
    all_sprites.add(player)
    ###
    push_trap_right1 = Enemy_Animations('SpriteSheet\Push_Trap_Right.png',366,672,0,0,player)
    push_trap_right2 = Enemy_Animations('SpriteSheet\Push_Trap_Right.png',366,706,0,0,player)
    spike_trap1 = Enemy_Animations('SpriteSheet\Spike_Trap.png',187,508,6,0,player)
    spike_trap2 = Enemy_Animations('SpriteSheet\Spike_Trap.png',157,508,6,0,player)
    spike_trap3 = Enemy_Animations('SpriteSheet\Spike_Trap.png',127,508,6,0,player)
    spike_trap4 = Enemy_Animations('SpriteSheet\Spike_Trap.png',97,508,6,0,player)
    spike_trap5 = Enemy_Animations('SpriteSheet\Spike_Trap.png',67,508,6,0,player)
    spike_trap6 = Enemy_Animations('SpriteSheet\Spike_Trap.png',157,478,0,0,player)
    spike_trap7 = Enemy_Animations('SpriteSheet\Spike_Trap.png',97,478,0,0,player)
    spike_trap8 = Enemy_Animations('SpriteSheet\Spike_Trap.png',187,448,6,0,player)
    spike_trap9 = Enemy_Animations('SpriteSheet\Spike_Trap.png',157,448,6,0,player)
    spike_trap10 = Enemy_Animations('SpriteSheet\Spike_Trap.png',127,448,6,0,player)
    spike_trap11 = Enemy_Animations('SpriteSheet\Spike_Trap.png',97,448,6,0,player)
    spike_trap12 = Enemy_Animations('SpriteSheet\Spike_Trap.png',67,448,6,0,player)
    spike_trap13 = Enemy_Animations('SpriteSheet\Spike_Trap.png',367,210,6,0,player,freeze = True)
    arrow_trap1 = Enemy_Animations('SpriteSheet\Arrow_Trap.png',500,603,3,280,player)
    arrow_trap2 = Enemy_Animations('SpriteSheet\Arrow_Trap.png',500,573,0,280,player)
    arrow_trap3 = Enemy_Animations('SpriteSheet\Arrow_Trap.png',500,543,5,25,player)
    arrow_trap4 = Enemy_Animations('SpriteSheet\Arrow_Trap.png',187,388,3,25,player)
    arrow_trap5 = Enemy_Animations('SpriteSheet\Arrow_Trap.png',187,358,0,25,player)
    arrow_trap6 = Enemy_Animations('SpriteSheet\Arrow_Trap.png',187,328,5,25,player)
    arrow_trap7 = Enemy_Animations('SpriteSheet\Arrow_Trap.png',187,298,0,25,player)
    arrow_trap8 = Enemy_Animations('SpriteSheet\Arrow_Trap.png',187,268,5,25,player)
    fire_trap1 = Enemy_Animations('SpriteSheet\Fire_Trap.png',270,630,0,0,player)
    fire_trap2 = Enemy_Animations('SpriteSheet\Fire_Trap.png',300,630,0,0,player)
    fire_trap3 = Enemy_Animations('SpriteSheet\Fire_Trap.png',330,630,7,0,player)
    fire_trap4 = Enemy_Animations('SpriteSheet\Fire_Trap.png',407,695,0,0,player)
    fire_trap5 = Enemy_Animations('SpriteSheet\Fire_Trap.png',436,695,7,0,player)
    object_list.append(push_trap_right1)
    object_list.append(push_trap_right2)
    object_list.append(spike_trap1)
    object_list.append(spike_trap2)
    object_list.append(spike_trap3)
    object_list.append(spike_trap4)
    object_list.append(spike_trap5)
    object_list.append(spike_trap6)
    object_list.append(spike_trap7)
    object_list.append(spike_trap8)
    object_list.append(spike_trap9)
    object_list.append(spike_trap10)
    object_list.append(spike_trap11)
    object_list.append(spike_trap12)
    object_list.append(spike_trap13)
    object_list.append(arrow_trap1)
    object_list.append(arrow_trap2)
    object_list.append(arrow_trap3)
    object_list.append(arrow_trap4)
    object_list.append(arrow_trap5)
    object_list.append(arrow_trap6)
    object_list.append(arrow_trap7)
    object_list.append(arrow_trap8)
    object_list.append(fire_trap1)
    object_list.append(fire_trap2)
    object_list.append(fire_trap3)
    object_list.append(fire_trap4)
    object_list.append(fire_trap5)
    
    return object_list ##inicjacja sprite'ów
###
###
my_spritesheet = Spritesheet('SpriteSheet\Sprite_sheet.png')
map = TileMap('Map\FINAL_MAP.csv',my_spritesheet)
object_list = Sprites_init()
###

def Screen_draw(player,screen,x,y):
    fake_screen = screen.copy()
    fake_screen.fill('black')
    fake_screen.blit(canvas,(x,y))
    screen.blit(pygame.transform.scale(fake_screen, (2048,1532)), (0, 0)) #nasza 'kamera'

def Screen_y_update(player,y):
    if y > -2:
        if y - (-player.rect.y) > 230:
            y-=2.5
    elif y < -376:
        if y - (-player.rect.y) < 130:
            y+=2.5
    else:
        if y - (-player.rect.y) < 130:
            y+=2.5
        elif y - (-player.rect.y) > 230:
            y-=2.5
    return y #poruszanie się kamery po osi y

def Screen_x_update(player,x):
    if x > 0:
        if x + player.rect.x > 330:
            x-=2.5
    elif x < - 511:
        if x + player.rect.x < 250:
            x+=2.5
    else:
        if x + player.rect.x > 330:
            x-=2.5
        elif x+player.rect.x < 250:
            x+=2.5
    return x # poruszanie sie kamery po osi x

def Sprites_update(object_list):
    for i in range(len(object_list)):
        object_list[i].refresh(canvas) #update sprite'ów


while(running == True):
    clock.tick(60)
    canvas=pygame.image.load('Floor.png').convert()
    if pygame.sprite.spritecollideany(player,enemies):
        player.rect.x = player.starting_x
        player.rect.y = player.starting_y
        enemies.remove(enemy1)
        enemy1 = Moving_Enemy(300,120)
        enemies.add(enemy1)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
                running = False
    
    player.update(pygame.key.get_pressed(), map.tiles)
    enemies.update(canvas,player,map.tiles)
    checkpoint1.update(canvas,player)
    checkpoint2.update(canvas,player)
    map.draw_map(canvas)
    Sprites_update(object_list)
    for entity in all_sprites:
        canvas.blit(entity.image,entity.rect)
    Screen_draw(player,screen,fake_width,fake_height)
    fake_height = Screen_y_update(player, fake_height)
    fake_width = Screen_x_update(player, fake_width)
    #screen.blit(canvas,(0,0))
    pygame.display.flip()

pygame.quit()


import pygame, csv
from pygame.locals import (RLEACCEL,KEYDOWN,K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,K_SPACE,QUIT)
from SpriteSheet.sprite_sheet import Spritesheet
from Map.Map import TileMap, Tile

WIDTH = 1024
HEIGHT = 768

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Player,self).__init__()
        player = Spritesheet('SpriteSheet\Player.png')
        self.starting_x = x
        self.starting_y = y
        self.stamina = 60
        self.attack_l_cnt = 0
        self.attack_r_cnt = 0
        self.attack_d_cnt = 0
        self.attack_u_cnt = 0
        self.is_attack_l = False
        self.is_attack_r = False
        self.is_attack_d = False
        self.is_attack_u = False
        self.attack = False
        self.attack_range_x = 0
        self.attack_range_y = 0
        self.x_change = 0
        self.y_change = 0
        self.stamina = 100
        self.standing_animation(player)
        self.moving_right_animation(player)
        self.moving_left_animation(player)
        self.moving_up_animation(player)
        self.moving_down_animation(player)
        self.basic_right_attack_animation(player)
        self.basic_up_attack_animation(player)
        self.basic_left_attack_animation(player)
        self.basic_down_attack_animation(player)

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def basic_down_attack_animation(self,player):
        self.basic_down_attack_animation = []
        self.basic_down_attack_animation.append(player.parse_sprite('Player_basic_down_attack1.png'))
        self.basic_down_attack_animation.append(player.parse_sprite('Player_basic_down_attack2.png'))
        self.basic_down_attack_animation.append(player.parse_sprite('Player_basic_down_attack3.png'))
        self.basic_down_attack_animation.append(player.parse_sprite('Player_basic_down_attack4.png'))
        self.basic_down_attack_animation.append(player.parse_sprite('Player_basic_down_attack5.png'))
        self.basic_down_attack_animation.append(player.parse_sprite('Player_basic_down_attack6.png'))
        self.cnt = 0
        self.image = self.basic_down_attack_animation[self.cnt]
        self.rect = self.image.get_rect()

    def basic_down_attack_update(self):
        if self.attack_d_cnt >= len(self.basic_down_attack_animation)-1:
            self.is_attack_d = False
            self.attack_d_cnt = 0
        elif self.attack_d_cnt < len(self.basic_down_attack_animation)-1 and self.is_attack_d == True:
            self.attack_d_cnt += 0.2
            self.image = self.basic_down_attack_animation[int(self.attack_d_cnt)]

    def basic_left_attack_animation(self,player):
        self.basic_left_attack_animation = []
        self.basic_left_attack_animation.append(player.parse_sprite('Player_basic_left_attack1.png'))
        self.basic_left_attack_animation.append(player.parse_sprite('Player_basic_left_attack2.png'))
        self.basic_left_attack_animation.append(player.parse_sprite('Player_basic_left_attack3.png'))
        self.basic_left_attack_animation.append(player.parse_sprite('Player_basic_left_attack4.png'))
        self.basic_left_attack_animation.append(player.parse_sprite('Player_basic_left_attack5.png'))
        self.basic_left_attack_animation.append(player.parse_sprite('Player_basic_left_attack6.png'))
        self.cnt = 0
        self.image = self.basic_left_attack_animation[self.cnt]
        self.rect = self.image.get_rect()

    def basic_left_attack_update(self):
        if self.attack_l_cnt >= len(self.basic_left_attack_animation)-1:
            self.is_attack_l = False
            self.attack_l_cnt = 0
        elif self.attack_l_cnt < len(self.basic_left_attack_animation)-1 and self.is_attack_l == True:
            self.attack_l_cnt += 0.2
            self.image = self.basic_left_attack_animation[int(self.attack_l_cnt)]

    def basic_up_attack_animation(self,player):
        self.basic_up_attack_animation = []
        self.basic_up_attack_animation.append(player.parse_sprite('Player_basic_up_attack1.png'))
        self.basic_up_attack_animation.append(player.parse_sprite('Player_basic_up_attack2.png'))
        self.basic_up_attack_animation.append(player.parse_sprite('Player_basic_up_attack3.png'))
        self.basic_up_attack_animation.append(player.parse_sprite('Player_basic_up_attack4.png'))
        self.basic_up_attack_animation.append(player.parse_sprite('Player_basic_up_attack5.png'))
        self.basic_up_attack_animation.append(player.parse_sprite('Player_basic_up_attack6.png'))
        self.cnt = 0
        self.image = self.basic_up_attack_animation[self.cnt]
        self.rect = self.image.get_rect()

    def basic_up_attack_update(self):
        if self.attack_u_cnt >= len(self.basic_up_attack_animation)-1:
            self.is_attack_u = False
            self.attack_u_cnt = 0
        elif self.attack_u_cnt < len(self.basic_up_attack_animation)-1 and self.is_attack_u == True:
            self.attack_u_cnt += 0.2
            self.image = self.basic_up_attack_animation[int(self.attack_u_cnt)]

    def basic_right_attack_animation(self,player):
        self.basic_right_attack_animation = []
        self.basic_right_attack_animation.append(player.parse_sprite('Player_basic_right_attack1.png'))
        self.basic_right_attack_animation.append(player.parse_sprite('Player_basic_right_attack2.png'))
        self.basic_right_attack_animation.append(player.parse_sprite('Player_basic_right_attack3.png'))
        self.basic_right_attack_animation.append(player.parse_sprite('Player_basic_right_attack4.png'))
        self.basic_right_attack_animation.append(player.parse_sprite('Player_basic_right_attack5.png'))
        self.basic_right_attack_animation.append(player.parse_sprite('Player_basic_right_attack6.png'))
        self.cnt = 0
        self.image = self.basic_right_attack_animation[self.cnt]
        self.rect = self.image.get_rect()

    def basic_right_attack_update(self):
        if self.attack_r_cnt >= len(self.basic_right_attack_animation)-1:
            self.is_attack_r = False
            self.attack_r_cnt = 0
        elif self.attack_r_cnt < len(self.basic_right_attack_animation)-1 and self.is_attack_r == True:
            self.attack_r_cnt += 0.2
            self.image = self.basic_right_attack_animation[int(self.attack_r_cnt)]

    def standing_animation(self,player):
        self.stand_animation = []
        self.stand_animation.append(player.parse_sprite('Player_stay1.png'))
        self.stand_animation.append(player.parse_sprite('Player_stay2.png'))
        self.stand_animation.append(player.parse_sprite('Player_stay3.png'))
        self.stand_animation.append(player.parse_sprite('Player_stay4.png'))
        self.stand_animation.append(player.parse_sprite('Player_stay5.png'))
        self.cnt = 0
        self.image = self.stand_animation[self.cnt]
        self.rect = self.image.get_rect()

    def stand_update(self):
        if self.cnt >= len(self.stand_animation)-1:
            self.cnt = 0
            self.image = self.stand_animation[self.cnt]
        else:
            self.cnt+=0.1
            self.image = self.stand_animation[int(self.cnt)]
    
    def moving_right_animation(self,player):
        self.move_right_animation = []
        self.move_right_animation.append(player.parse_sprite('Player_move_right1.png'))
        self.move_right_animation.append(player.parse_sprite('Player_move_right2.png'))
        self.move_right_animation.append(player.parse_sprite('Player_move_right3.png'))
        self.move_right_animation.append(player.parse_sprite('Player_move_right4.png'))
        self.move_right_animation.append(player.parse_sprite('Player_move_right5.png'))
        self.move_right_animation.append(player.parse_sprite('Player_move_right6.png'))
        self.move_right_animation.append(player.parse_sprite('Player_move_right7.png'))
        self.move_right_animation.append(player.parse_sprite('Player_move_right8.png'))
        self.cnt = 0
        self.image = self.move_right_animation[self.cnt]
        self.rect = self.image.get_rect()

    def moving_left_animation(self,player):
        self.move_left_animation = []
        self.move_left_animation.append(player.parse_sprite('Player_move_left1.png'))
        self.move_left_animation.append(player.parse_sprite('Player_move_left2.png'))
        self.move_left_animation.append(player.parse_sprite('Player_move_left3.png'))
        self.move_left_animation.append(player.parse_sprite('Player_move_left4.png'))
        self.move_left_animation.append(player.parse_sprite('Player_move_left5.png'))
        self.move_left_animation.append(player.parse_sprite('Player_move_left6.png'))
        self.move_left_animation.append(player.parse_sprite('Player_move_left7.png'))
        self.move_left_animation.append(player.parse_sprite('Player_move_left8.png'))
        self.cnt = 0
        self.image = self.move_left_animation[self.cnt]
        self.rect = self.image.get_rect()

    def moving_up_animation(self,player):
        self.move_up_animation = []
        self.move_up_animation.append(player.parse_sprite('Player_move_up1.png'))
        self.move_up_animation.append(player.parse_sprite('Player_move_up2.png'))
        self.move_up_animation.append(player.parse_sprite('Player_move_up3.png'))
        self.move_up_animation.append(player.parse_sprite('Player_move_up4.png'))
        self.move_up_animation.append(player.parse_sprite('Player_move_up5.png'))
        self.move_up_animation.append(player.parse_sprite('Player_move_up6.png'))
        self.move_up_animation.append(player.parse_sprite('Player_move_up7.png'))
        self.move_up_animation.append(player.parse_sprite('Player_move_up8.png'))
        self.cnt = 0
        self.image = self.move_up_animation[self.cnt]
        self.rect = self.image.get_rect()

    def moving_down_animation(self,player):
        self.move_down_animation = []
        self.move_down_animation.append(player.parse_sprite('Player_move_down1.png'))
        self.move_down_animation.append(player.parse_sprite('Player_move_down2.png'))
        self.move_down_animation.append(player.parse_sprite('Player_move_down3.png'))
        self.move_down_animation.append(player.parse_sprite('Player_move_down4.png'))
        self.move_down_animation.append(player.parse_sprite('Player_move_down5.png'))
        self.move_down_animation.append(player.parse_sprite('Player_move_down6.png'))
        self.move_down_animation.append(player.parse_sprite('Player_move_down7.png'))
        self.move_down_animation.append(player.parse_sprite('Player_move_down8.png'))
        self.cnt = 0
        self.image = self.move_down_animation[self.cnt]
        self.rect = self.image.get_rect()
    
    def move_down_update(self):
        if self.cnt >= len(self.move_down_animation)-1:
            self.cnt = 0
            self.image = self.move_down_animation[self.cnt]
        else:
            self.cnt+=0.1
            self.image = self.move_down_animation[int(self.cnt)]

    def move_up_update(self):
        if self.cnt >= len(self.move_up_animation)-1:
            self.cnt = 0
            self.image = self.move_up_animation[self.cnt]
        else:
            self.cnt+=0.1
            self.image = self.move_up_animation[int(self.cnt)]

    def move_left_update(self):
        if self.cnt >= len(self.move_left_animation)-1:
            self.cnt = 0
            self.image = self.move_left_animation[self.cnt]
        else:
            self.cnt+=0.08
            self.image = self.move_left_animation[int(self.cnt)]

    def move_right_update(self):
        if self.cnt >= len(self.move_right_animation)-1:
            self.cnt = 0
            self.image = self.move_right_animation[self.cnt]
        else:
            self.cnt+=0.1
            self.image = self.move_right_animation[int(self.cnt)]

    def update(self,key_pressed,tiles):
        if self.stamina < 100:
            self.stamina += 2
        self.stand_update()
        self.attack_range_x = 0
        self.attack_range_y = 0
        if self.y_change < 0:
            self.basic_up_attack(key_pressed)
        elif self.x_change < 0:
            self.basic_left_attack(key_pressed)
        elif self.x_change > 0:
            self.basic_right_attack(key_pressed)
        elif self.y_change > 0:
            self.basic_down_attack(key_pressed)
        self.attack_hitbox()
        self.y_move(key_pressed)
        self.collision_check('y',tiles)
        self.x_move(key_pressed)
        self.collision_check('x',tiles) #metoda aktualizuje parametry gracz

    def attack_hitbox(self):
        if self.is_attack_r == True:
            self.attack_range_x = 6
            self.attack_range_y = 3
        if self.is_attack_l == True:
            self.attack_range_x = 3
            self.attack_range_y = 1.5
    
    def basic_right_attack(self,key_pressed):
        if self.stamina >= 100:
            if key_pressed[K_SPACE]:
                self.is_attack_r = True
                self.stamina = 0
        self.basic_right_attack_update()

    def basic_up_attack(self,key_pressed):
         if key_pressed[K_SPACE]:
             self.is_attack_u = True
         self.basic_up_attack_update()

    def basic_left_attack(self,key_pressed):
         if key_pressed[K_SPACE]:
             self.is_attack_l = True
         self.basic_left_attack_update()

    def basic_down_attack(self,key_pressed):
         if key_pressed[K_SPACE]:
             self.is_attack_d = True
         self.basic_down_attack_update()

    def y_move(self,key_pressed):
         self.y_change = 0
         if key_pressed[K_DOWN]:
            self.y_change = 3
            self.rect.move_ip(0,self.y_change)
            self.move_down_update()
         elif key_pressed[K_UP]:
            self.y_change = -3
            self.rect.move_ip(0,self.y_change)
            self.move_up_update()

    def x_move(self,key_pressed):
        if key_pressed[K_LEFT]:
            self.x_change = -3
            self.rect.move_ip(self.x_change,0)
            self.move_left_update()
        elif key_pressed[K_RIGHT]:
            self.x_change = 3
            self.rect.move_ip(self.x_change,0)
            self.move_right_update()

    def get_hits(self, tiles):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits

    def collision_check(self,direction,tiles):
        hits = self.get_hits(tiles)
        if direction == 'x':
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change <0:
                    self.rect.x = hits[0].rect.right
        elif direction == 'y': 
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change <0:
                    self.rect.y = hits[0].rect.bottom #klasa gracz

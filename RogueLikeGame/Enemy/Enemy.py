import pygame 
from SpriteSheet.sprite_sheet import Spritesheet
from Player.Player import Player

WIDTH = 1024
HEIGHT = 768

enemies = pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
key_enemies = pygame.sprite.Group()

class Checkpoint(pygame.sprite.Sprite): #checkpoint
    def __init__(self,x,y):
        super(Checkpoint,self).__init__()
        self.x = x
        self.y = y
        checkpoint_before = Spritesheet('SpriteSheet\CheckPoint.png')
        self.image = checkpoint_before.parse_sprite('CheckPoint_before.png')
        self.rect = self.image.get_rect(center = (self.x,self.y))

    def Collision_detect(self,player):
        if pygame.Rect.colliderect(self.rect,player):
            checkpoint_after = Spritesheet('SpriteSheet\Checkpoint.png')
            self.image = checkpoint_after.parse_sprite('CheckPoint_after.png')
            self.rect = self.image.get_rect(center = (self.x,self.y))
            player.starting_x = self.x
            player.starting_y = self.y

    def update(self,display,player):
        self.Collision_detect(player)
        self.draw(display)

    def draw(self,display):
           display.blit(self.image, (self.rect.x, self.rect.y))

class Moving_Enemy(pygame.sprite.Sprite): #tworzy przeciwnika
    def __init__(self,x,y):
        super(Moving_Enemy,self).__init__()
        self.x = x
        self.y = y
        self.x_cnt = 0
        self.y_cnt = 0
        self.aggro = False
        self.starting_coo = True
        self.direction = 'right'
        self.hp = 1000
        enemy = Spritesheet('SpriteSheet\Slime.png')
        self.Move_Left_animation(enemy)
        self.Move_Right_animation(enemy)
        self.Move_Down_animation(enemy)
        self.Move_Up_animation(enemy)
        self.rect.x = self.x
        self.rect.y = self.y 


    def Move_Left_animation(self, enemy):
        self.move_left_anim = []
        self.move_left_anim.append(enemy.parse_sprite('Slime_left1.png'))
        self.move_left_anim.append(enemy.parse_sprite('Slime_left2.png'))
        self.move_left_anim.append(enemy.parse_sprite('Slime_left3.png'))
        self.move_left_anim.append(enemy.parse_sprite('Slime_left4.png'))
        self.cnt = 0
        self.image = self.move_left_anim[self.cnt]
        self.rect = self.image.get_rect()

    def Move_Right_animation(self, enemy):
        self.move_right_anim = []
        self.move_right_anim.append(enemy.parse_sprite('Slime_right1.png'))
        self.move_right_anim.append(enemy.parse_sprite('Slime_right2.png'))
        self.move_right_anim.append(enemy.parse_sprite('Slime_right3.png'))
        self.move_right_anim.append(enemy.parse_sprite('Slime_right4.png'))
        self.cnt = 0
        self.image = self.move_right_anim[self.cnt]
        self.rect = self.image.get_rect()

    def Move_Down_animation(self, enemy):
        self.move_down_anim = []
        self.move_down_anim.append(enemy.parse_sprite('Slime_down1.png'))
        self.move_down_anim.append(enemy.parse_sprite('Slime_down2.png'))
        self.move_down_anim.append(enemy.parse_sprite('Slime_down3.png'))
        self.move_down_anim.append(enemy.parse_sprite('Slime_down4.png'))
        self.cnt = 0
        self.image = self.move_down_anim[self.cnt]
        self.rect = self.image.get_rect()

    def Move_Up_animation(self, enemy):
        self.move_up_anim = []
        self.move_up_anim.append(enemy.parse_sprite('Slime_up1.png'))
        self.move_up_anim.append(enemy.parse_sprite('Slime_up2.png'))
        self.move_up_anim.append(enemy.parse_sprite('Slime_up3.png'))
        self.move_up_anim.append(enemy.parse_sprite('Slime_up4.png'))
        self.cnt = 0
        self.image = self.move_up_anim[self.cnt]
        self.rect = self.image.get_rect()

    def move_up_update(self):
        if self.cnt >= len(self.move_up_anim)-1:
            self.cnt = 0
            self.image = self.move_up_anim[self.cnt]
        else:
            self.cnt+=0.1
            self.image = self.move_up_anim[int(self.cnt)]

    def move_down_update(self):
        if self.cnt >= len(self.move_down_anim)-1:
            self.cnt = 0
            self.image = self.move_down_anim[self.cnt]
        else:
            self.cnt+=0.1
            self.image = self.move_down_anim[int(self.cnt)]

    def move_right_update(self):
        if self.cnt >= len(self.move_right_anim)-1:
            self.cnt = 0
            self.image = self.move_right_anim[self.cnt]
        else:
            self.cnt+=0.1
            self.image = self.move_right_anim[int(self.cnt)]

    def move_left_update(self):
        if self.cnt >= len(self.move_left_anim)-1:
            self.cnt = 0
            self.image = self.move_left_anim[self.cnt]
        else:
            self.cnt+=0.1
            self.image = self.move_left_anim[int(self.cnt)]

    def draw(self,display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def movement(self):
        if self.direction == 'right' or self.direction == 'up' or self.direction == 'down':
            self.rect.x += 1
            self.x_cnt += 1
            if self.x_cnt > 60:
                self.direction = 'left'
        elif self.direction == 'left':
            self.rect.x -=1
            self.x_cnt -= 1
            if self.x_cnt < 0:
                self.direction = 'right'

    def player_detect(self,player):
        self.space_beetwen_x = abs(self.rect.x - player.rect.x)
        self.space_beetwen_y = abs(self.rect.y - player.rect.y)
        if self.space_beetwen_x < 50 and self.space_beetwen_y < 50:
            self.aggro = True

    def player_chase(self,player,tiles):
        self.player_detect(player)
        if self.aggro == True:
             if player.rect.x < self.rect.x:
                self.x_change = -1
                self.rect.x += self.x_change
                self.collision_check('x',tiles)
                self.direction = 'left'
             if player.rect.x > self.rect.x:
                self.x_change = 1
                self.rect.x += self.x_change
                self.collision_check('x',tiles)
                self.direction = 'right'
             if player.rect.y > self.rect.y:
                self.y_change = 1
                self.rect.y += self.y_change
                self.collision_check('y',tiles)
                self.direction = 'down'
             if player.rect.y < self.rect.y:
                self.y_change = -1
                self.rect.y += self.y_change
                self.collision_check('y',tiles)
                self.direction = 'up'

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
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        elif direction == 'y': 
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change <0:
                    self.rect.y = hits[0].rect.bottom

    def Back_to_start(self):
        if self.rect.x < self.x:
            self.rect.x +=1
        if self.rect.x > self.x:
            self.rect.x -=1
        if self.rect.y < self.y:
            self.rect.y +-1
        if self.rect.y > self.y:
            self.rect.y -=1
        if self.rect.y == self.y and self.rect.x == self.x:
            self.starting_coo = True

    def is_in_attack_range(self,player):
        if self.rect.left < (player.rect.right + player.attack_range_x) and self.rect.left > player.rect.right:
            self.hp -= 20
            self.rect.x += 1
        if self.rect.right > (player.rect.left - player.attack_range_x) and self.rect.right < player.rect.left:
            self.hp -= 20
            self.rect.x -= 1

    def dead(self):
        if self.hp <= 0:
            enemies.remove(self)
    
    def update(self,display,player,tiles):
        if self.starting_coo == False:
            self.Back_to_start()
        if self.aggro == False and self.starting_coo == True:
            self.movement()
        self.player_chase(player,tiles)
        if self.direction == 'left':
            self.move_left_update()
        if self.direction == 'right':
            self.move_right_update()
        if self.direction == 'up':
            self.move_up_update()
        if self.direction == 'down':
            self.move_down_update()
        if player.rect.y > 240 and self.aggro == True:
            self.aggro = False
            self.starting_coo = False
        self.draw(display)
        self.is_in_attack_range(player)
        self.dead()



class Enemy(pygame.sprite.Sprite): #tworzy pułapke skaldajaca sie z pojedynczego obrazu
    def __init__(self,filename,x,y,x_kill):
        super(Enemy,self).__init__()
        self.filename = filename
        self.x_kill = x_kill
        if self.filename == 'Enemy\Arrow.png':
            self.image = pygame.image.load(filename).convert()
            self.rect = self.image.get_rect(center = (x,y))
        elif self.filename == 'Enemy\Pit_Trap_Spikes.png':
            self.image = pygame.image.load(filename).convert()
            self.rect = self.image.get_rect(center = (x,y))

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def update(self,display,player,tiles):
        if self.filename == 'Enemy\Arrow.png':
            self.rect.move_ip(-5,0)
        if self.rect.x < self.x_kill:
            self.kill()
        self.draw(display)

class Enemy_Animations(pygame.sprite.Sprite): #tworzy pułapke skaldajaca sie z animacji
     def __init__(self,filename,x,y,cnt,x_kill,player,freeze = False):
        super(Enemy_Animations,self).__init__()
        self.filename = filename
        self.x_coo = x
        self.y_coo = y
        self.cnt = cnt
        self.player = player
        self.x_kill = x_kill
        self.freeze = freeze
        if self.filename == 'SpriteSheet\Arrow_Trap.png':
            arrow_trap = Spritesheet('SpriteSheet\Arrow_Trap.png')
            self.Arrow_Trap_animation(arrow_trap)
        elif self.filename == 'SpriteSheet\Fire_Trap.png':
            fire_trap = Spritesheet('SpriteSheet\Fire_Trap.png')
            self.Fire_Trap_animation(fire_trap)
        elif self.filename == 'SpriteSheet\Push_Trap_Right.png':
            push_trap_right = Spritesheet('SpriteSheet\Push_Trap_Right.png')
            self.Push_Trap_Right_animation(push_trap_right)
        elif self.filename == 'SpriteSheet\Spike_Trap.png':
            spike_trap = Spritesheet('SpriteSheet\Spike_Trap.png')
            self.Spike_Trap_animation(spike_trap)
        self.arrow = Enemy('Enemy\Arrow.png',self.x_coo-32,self.y_coo-2,self.x_kill)

     def Spike_Trap_animation(self,spike_trap):
            self.Spike_Trap_anim = []
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap1.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap2.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap3.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap4.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap5.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap6.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap7.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap8.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap9.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap10.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap11.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap12.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap13.png'))
            self.Spike_Trap_anim.append(spike_trap.parse_sprite('Spike_Trap14.png'))
            self.image = self.Spike_Trap_anim[self.cnt]
            self.rect = self.image.get_rect(center = (self.x_coo,self.y_coo))

     def Spike_Trap_update(self,display):
        if self.freeze == False:
            if self.cnt >= len(self.Spike_Trap_anim)-1:
                self.cnt = 0
                self.image = self.Spike_Trap_anim[self.cnt]
            elif self.cnt > 9 and self.cnt <= 10:
                enemies.add(self)
                self.cnt += 0.1
                self.image = self.Spike_Trap_anim[int(self.cnt)]
            elif self.cnt > 11:
                enemies.remove(self)
                self.cnt += 0.1
                self.image = self.Spike_Trap_anim[int(self.cnt)]
            else:
                self.cnt+=0.1
                self.image = self.Spike_Trap_anim[int(self.cnt)]
        elif self.freeze == True:
            enemies.add(self)
            self.image = self.Spike_Trap_anim[9]

     def Push_Trap_Right_animation(self,push_trap_right):
        self.Push_Trap_Right_anim = []
        self.Push_Trap_Right_anim.append(push_trap_right.parse_sprite('Push_Trap_Right1.png'))
        self.Push_Trap_Right_anim.append(push_trap_right.parse_sprite('Push_Trap_Right2.png'))
        self.Push_Trap_Right_anim.append(push_trap_right.parse_sprite('Push_Trap_Right3.png'))
        self.Push_Trap_Right_anim.append(push_trap_right.parse_sprite('Push_Trap_Right4.png'))
        self.Push_Trap_Right_anim.append(push_trap_right.parse_sprite('Push_Trap_Right5.png'))
        self.Push_Trap_Right_anim.append(push_trap_right.parse_sprite('Push_Trap_Right6.png'))
        self.Push_Trap_Right_anim.append(push_trap_right.parse_sprite('Push_Trap_Right7.png'))
        self.Push_Trap_Right_anim.append(push_trap_right.parse_sprite('Push_Trap_Right8.png'))
        self.Push_Trap_Right_anim.append(push_trap_right.parse_sprite('Push_Trap_Right9.png'))
        self.Push_Trap_Right_anim.append(push_trap_right.parse_sprite('Push_Trap_Right10.png'))
        self.Push_Trap_Right_anim.append(push_trap_right.parse_sprite('Push_Trap_Right11.png'))
        self.image = self.Push_Trap_Right_anim[self.cnt]
        self.rect = self.image.get_rect(center = (self.x_coo,self.y_coo))

     def Push_Trap_Right_update(self,display):
        if self.cnt >= len(self.Push_Trap_Right_anim)-1:
            self.cnt = 0
        elif self.cnt > 4 and self.cnt < 9:
            self.cnt+=0.1
            self.image = self.Push_Trap_Right_anim[int(self.cnt)]
            if self.rect.colliderect(self.player):
                if self.player.y_change < 0:
                    self.player.rect.y = self.rect.bottom
                elif self.player.y_change > 0:
                    self.player.rect.y = self.rect.top - self.player.rect.height
                elif self.player.y_change == 0:
                    self.player.rect.x += 5
        else:
            self.cnt+=0.1
            self.image = self.Push_Trap_Right_anim[int(self.cnt)]


     def Fire_Trap_animation(self,fire_trap):
        self.Fire_Trap_anim = []
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap1.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap2.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap3.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap4.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap5.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap6.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap7.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap8.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap9.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap10.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap11.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap12.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap13.png'))
        self.Fire_Trap_anim.append(fire_trap.parse_sprite('Fire_Trap14.png'))
        self.image = self.Fire_Trap_anim[self.cnt]
        self.rect = self.image.get_rect(center = (self.x_coo,self.y_coo))

     def Fire_Trap_update(self,display):
        if self.cnt >= len(self.Fire_Trap_anim)-1:
            self.cnt = 0
            self.image = self.Fire_Trap_anim[self.cnt]
        elif self.cnt > 8 and self.cnt <= 10:
            enemies.add(self)
            self.cnt += 0.1
            self.image = self.Fire_Trap_anim[int(self.cnt)]
        elif self.cnt > 11:
             enemies.remove(self)
             self.cnt += 0.1
             self.image = self.Fire_Trap_anim[int(self.cnt)]
        else:
            self.cnt+=0.1
            self.image = self.Fire_Trap_anim[int(self.cnt)]

     def Arrow_Trap_animation(self,arrow_trap):
        self.Arrow_Trap_anim = []
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap1.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap2.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap3.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap4.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap5.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap6.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap7.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap8.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap9.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap10.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap11.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap12.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap13.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap14.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap15.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap16.png'))
        self.Arrow_Trap_anim.append(arrow_trap.parse_sprite('Arrow_Trap17.png'))
        enemies.add(self)
        self.image = self.Arrow_Trap_anim[self.cnt]
        self.rect = self.image.get_rect(center = (self.x_coo,self.y_coo))

     def Arrow_Trap_update(self,display):
        if self.cnt >= len(self.Arrow_Trap_anim)-1:
            self.cnt = 0
            self.image = self.Arrow_Trap_anim[self.cnt]
        elif self.cnt > 9 and self.cnt < 10:
           self.arrow = Enemy('Enemy\Arrow.png',self.x_coo-32,self.y_coo,self.x_kill)
           enemies.add(self.arrow)
           all_sprites.add(self.arrow)
           self.cnt = 10
        else:
            self.cnt+=0.15
            self.image = self.Arrow_Trap_anim[int(self.cnt)]

     def refresh(self, display):
         if self.filename == 'SpriteSheet\Arrow_Trap.png':
             self.Arrow_Trap_update(display)
             self.draw(display)
         elif self.filename == 'SpriteSheet\Fire_Trap.png':
             self.Fire_Trap_update(display)
             self.draw(display)
         elif self.filename == 'SpriteSheet\Push_Trap_Right.png':
             self.Push_Trap_Right_update(display)
             self.draw(display)
         elif self.filename == 'SpriteSheet\Spike_Trap.png':
             self.Spike_Trap_update(display)
             self.draw(display)

     def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
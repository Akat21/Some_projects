import pygame , csv, os
vec = pygame.math.Vector2

WIDTH = 1024
HEIGHT = 768

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y =x , y
        
    def draw(self,surface):
        surface.blit(self.image, (self.rect.x,self.rect.y)) #pobiera kafelek z pliku png

#class Camera:
    #def __init__(self,player):
       # self.player = player
       # self.offset = vec(0, 0)
      #  self.offset_float = vec(0, 0)
     #   self.DISPLAY_W, self.DISPLAY_H = 480, 270
        #self.CONST = vec(-self.DISPLAY_W / 2 + player.rect.w / 2, -self.player.ground_y + 20)

  #  def scroll(self):
        #self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        #self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
       # self.offset.x, self.offset.y = int(self.offset_float.x), int(self.offset_float.y)

class TileMap():
    def __init__(self,filename,spritesheet):
        self.tile_size = 16
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey(('black'))
        self.load_map()

    def draw_map(self,surface):
        surface.blit(self.map_surface,(0,0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def read_csv(self,filename):
        map =[]
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter = ',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self,filename):
        tiles = []
        map = self.read_csv(filename)
        x,y=0,0
        for row in map:
            x=0
            for tile in row:
                if tile == '0':
                    tiles.append(Tile('top_topleft_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '50':
                    tiles.append(Tile('top_bottomleft_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '52' or tile == '53':
                    tiles.append(Tile('upper_down_wall.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '42' or tile == '43' or tile == '7' or tile =='8':
                    tiles.append(Tile('bottom_down_wall.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '25' or tile == '35':
                    tiles.append(Tile('upper_right_wall.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '24' or tile == '34' or tile=='16' or tile =='26':
                    tiles.append(Tile('bottom_right_wall.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '2' or tile == '3':
                    tiles.append(Tile('upper_top_wall.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '12' or tile == '13' or tile == '37' or tile =='38':
                    tiles.append(Tile('bottom_top_wall.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '5':
                    tiles.append(Tile('top_topright_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '4':
                    tiles.append(Tile('left_topright_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '14':
                    tiles.append(Tile('bottom_topright_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '15':
                    tiles.append(Tile('right_topright_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '55':
                    tiles.append(Tile('top_bottomright_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '54':
                    tiles.append(Tile('left_bottomright_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '44':
                    tiles.append(Tile('bottom_bottomright_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '45':
                    tiles.append(Tile('right_bottomright_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '10':
                    tiles.append(Tile('left_topleft_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '1':
                    tiles.append(Tile('right_topleft_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '11':
                    tiles.append(Tile('bottom_topleft_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '49' or tile == '48' or tile == '59' or tile == '58':
                    tiles.append(Tile('top_wall.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '41':
                    tiles.append(Tile('bottom_bottomleft_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '40':
                    tiles.append(Tile('left_bottomleft_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '51':
                    tiles.append(Tile('right_bottomleft_column.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '30' or tile == '20':
                     tiles.append(Tile('upper_left_wall.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '31' or tile == '21' or tile =='29' or tile == '19':
                     tiles.append(Tile('bottom_left_wall.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '60':
                     tiles.append(Tile('bottomleft_bottom_doors.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '61':
                     tiles.append(Tile('bottommid_bottom_doors.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '62':
                     tiles.append(Tile('bottomright_bottom_doors.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '70':
                     tiles.append(Tile('upperleft_bottom_doors.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '71':
                     tiles.append(Tile('uppermid_bottom_doors.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '72':
                     tiles.append(Tile('upperright_bottom_doors.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '17':
                     tiles.append(Tile('upper_left_corner.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '18':
                     tiles.append(Tile('upper_right_corner.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '27':
                     tiles.append(Tile('bottom_left_corner.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '28':
                     tiles.append(Tile('bottom_right_corner.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '6':
                     tiles.append(Tile('upper_left_corner1.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '9':
                     tiles.append(Tile('upper_right_corner1.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '36':
                     tiles.append(Tile('bottom_left_corner1.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                elif tile == '39':
                     tiles.append(Tile('bottom_right_corner1.png',x*self.tile_size,y*self.tile_size, self.spritesheet))
                x += 1
            y += 1
        self.map_w,self.map_h = x*self.tile_size, y*self.tile_size
        return tiles #wypełnia mape kafelkami

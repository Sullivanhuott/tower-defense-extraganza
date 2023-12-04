import pygame as pg
import constants as c

class Ally(pg.sprite.Sprite):
    def __init__(self, image, tile_x, tile_y):
        pg.sprite.Sprite.__init__(self)
        self.tile_x = tile_x
        self.tile_y = tile_y
        #find center coords
        self.x = (self.tile_x + .5) * c.TILE_SIZE
        self.y = (self.tile_y + .5) * c.TILE_SIZE
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

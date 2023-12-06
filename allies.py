import pygame as pg
import constants as c
import math

class Ally(pg.sprite.Sprite):
    def __init__(self, image, tile_x, tile_y):
        pg.sprite.Sprite.__init__(self)
        self.upgrade_level = 1
        self.range = c.ALLY_DATA[self.upgrade_level - 1].get("range")
        self.cooldown = c.ALLY_DATA[self.upgrade_level - 1].get("cooldown")
        self.last_shot = pg.time.get_ticks()
        self.selected = False
        self.target = None


        #position variables
        self.tile_x = tile_x
        self.tile_y = tile_y
        #find center coords
        self.x = (self.tile_x + .5) * c.TILE_SIZE
        self.y = (self.tile_y + .5) * c.TILE_SIZE

        #update image
        self.angle = 90
        self.original_image = image
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        #create a transparent circle to show range
        self.range_image = pg.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0,0,0))
        self.range_image.set_colorkey((0,0,0))
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def update(self, enemy_group):
        if pg.time.get_ticks() - self.last_shot > self.cooldown:
            self.pick_target(enemy_group)

    def pick_target(self, enemy_group):
        #find enemy
        x_dist = 0
        y_dist = 0
        #check distance to each enemy to see if it is in range
        for enemy in enemy_group:
            x_dist = enemy.position[0] - self.x
            y_dist = enemy.position[1] - self.y
            dist = math.sqrt(x_dist ** 2 + y_dist ** 2)
            if dist < self.range:
                self.target = enemy
                self.angle = math.degrees(math.atan2(-y_dist, x_dist))
                print("target selected")

    def upgrade(self):
        self.upgrade_level += 1
        self.range = c.ALLY_DATA[self.upgrade_level - 1].get("range")
        self.cooldown = c.ALLY_DATA[self.upgrade_level - 1].get("cooldown")

        #upgraded range
        self.range_image = pg.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def draw(self, surface):
        self.image = pg.transform.rotate(self.original_image, self.angle-90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        surface.blit(self.image, self.rect)
        if self.selected == True:
            surface.blit(self.range_image, self.range_rect)